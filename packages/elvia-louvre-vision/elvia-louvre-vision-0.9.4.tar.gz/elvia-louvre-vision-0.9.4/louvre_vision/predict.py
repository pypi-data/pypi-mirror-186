"""Prediction-related module."""
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.prediction.models import Prediction, BoundingBox
from azure.cognitiveservices.vision.customvision.training.models import Iteration
from elvia_louvre.errors import LouvreImageNotFound
from elvia_louvre.image_api import ImageData
from elvia_louvre.louvre_client import LouvreClient
from typing import Dict, List, Optional

from louvre_vision.config import Config
from louvre_vision.data_models import AppProperties, ClassificationPredictionResult, CustomVisionPluginPredictionRequest, ImageRegion, MetadataEntry, ObjectDetectionPredictionResult, PluginEndpointRequest, PredictionResult, RegionBoundingBox, ResultBundle
from louvre_vision.images import ImageMethods
from louvre_vision.metadata import MetadataUpdater
from louvre_vision.methods import Methods


class ClassificationPrediction:
    """
    Class with methods to make classification predictions.
    """
    @staticmethod
    def classify_from_image_data(
        prediction_client: CustomVisionPredictionClient,
        model: Iteration,
        image_data: ImageData,
        probability_threshold: float = 0
    ) -> List[ClassificationPredictionResult]:
        """
        Classify and image and return predictions given a Custom Vision model.

        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param Iteration model: Published Custom Vision iteration
        :param ImageData image_data: Image data from a previous call to ImageAPI
        :param float probability_threshold: Filter out predictions below a probability cutoff value. Defaults to 0.

        :rtype: List[ClassificationPredictionResult]
        
        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreVisionValueError:
        :raises RequestException:
        """
        image_entry = ImageMethods.get_image_from_image_data(
            image_data=image_data,
            max_file_size=Config.custom_vision_max_prediction_file_size)
        if image_entry.is_empty:
            raise LouvreImageNotFound()
        predictions: List[Prediction]
        if image_entry.sasuri:
            predictions = prediction_client.classify_image_url_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                url=image_entry.sasuri).predictions
        else:
            predictions = prediction_client.classify_image_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                image_data=image_entry.file_bytes).predictions
        return ClassificationPrediction._extract_predictions_above_threshold(
            predictions=predictions,
            probability_threshold=probability_threshold)

    @staticmethod
    def classify_from_url(
        prediction_client: CustomVisionPredictionClient,
        model: Iteration,
        image_url: str,
        probability_threshold: float = 0
    ) -> List[ClassificationPredictionResult]:
        """
        Return classification predictions given a model and an image URL.

        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param Iteration model: Published Custom Vision iteration
        :param ImageData image_url: Image URL
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.

        :rtype: List[ObjectDetectionPredictionResult]

        :raises CustomVisionErrorException:
        :raises LouvreVisionValueError:
        :raises RequestException:
        """
        # Attempt to find out the image size without actually fetching it
        file_size = Methods.get_remote_file_size(file_url=image_url)
        predictions: List[Prediction]
        if file_size and file_size < Config.custom_vision_max_prediction_file_size:
            predictions = prediction_client.classify_image_url_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                url=image_url).predictions
        else:
            predictions = prediction_client.classify_image_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                image_data=ImageMethods.resize_from_url(
                    image_url=image_url,
                    image_longer_side=Config.image_longer_side)).predictions
        return ClassificationPrediction._extract_predictions_above_threshold(
            predictions=predictions,
            probability_threshold=probability_threshold)

    @staticmethod
    def classify(
        prediction_client: CustomVisionPredictionClient,
        louvre_client: LouvreClient,
        model: Iteration,
        image_identifier: str,
        using_production_images: bool = False,
        probability_threshold: float = 0
    ) -> List[ClassificationPredictionResult]:
        """
        Return classification predictions given a model and either an image URL or an ImageId
        
        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param LouvreClient louvre_client: LouvreClient instance with access to the Louvre environment where this image exists.
        :param Iteration model: Published Custom Vision iteration
        :param str image_identifier: Image URL or Louvre ImageId
        :param bool using_production_images: Whether to fetch images from production. Defaults to False.
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.


        :rtype: List[ObjectDetectionPredictionResult]

        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreKeyError:
        :raises LouvreQueryError:
        :raises LouvreVisionValueError:
        :raises RequestException:     
        """
        if Methods.is_string_url(input_str=image_identifier):
            return ClassificationPrediction.classify_from_url(
                prediction_client=prediction_client,
                model=model,
                image_url=image_identifier,
                probability_threshold=probability_threshold)
        image_data = louvre_client.get_image_data(
            image_id=image_identifier,
            using_production_images=using_production_images)
        return ClassificationPrediction.classify_from_image_data(
            prediction_client=prediction_client,
            model=model,
            image_data=image_data,
            probability_threshold=probability_threshold)

    @staticmethod
    def _extract_predictions_above_threshold(
        predictions: List[Prediction],
        probability_threshold: float = 0
    ) -> List[ClassificationPredictionResult]:
        """
        Return custom ClassificationPredictionResult objects given Custom Vision 
        predictions. Optionally discard predictions under a cutoff probability threshold.
        """
        result = []
        for prediction in predictions:
            if prediction.probability > probability_threshold:
                result.append(
                    ClassificationPredictionResult(
                        probability=prediction.probability,
                        tag_name=prediction.tag_name))
        return result

    @staticmethod
    def classify_and_update_metadata(
            prediction_client: CustomVisionPredictionClient,
            louvre_client: LouvreClient,
            endpoint_request: PluginEndpointRequest,
            model: Iteration,
            app_properties: AppProperties,
            probability_threshold: float = 0) -> None:
        """
        Classify an image and update the image metadata.
        Predictions are not run if a metadata entry already exists. 
        
        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param LouvreClient louvre_client: LouvreClient instance with access to the Louvre environment where this image exists.
        :param PluginEndpointRequest endpoint_request: Object containing all information about an incoming request.
        :param Iteration model: Published Custom Vision iteration
        :param AppProperties app_properties: Object that describes the application.
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.
        
        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreKeyError:
        :raises LouvreQueryError:
        :raises LouvreVisionValueError:
        :raises RequestException: 
        """
        image_data = louvre_client.get_image_data(
            image_id=endpoint_request.image_identifier)
        existing_entry = MetadataUpdater.exists(
            image_data=image_data,
            model_name=endpoint_request.model_name,
            app_name=app_properties.app_name,
            app_version=app_properties.app_version,
            iteration_publish_name=model.publish_name)
        if not existing_entry:
            predictions = ClassificationPrediction.classify_from_image_data(
                prediction_client=prediction_client,
                model=model,
                image_data=image_data,
                probability_threshold=probability_threshold)
            result = ClassificationPrediction._extract_most_likely_category(
                predictions, probability_threshold)
            result_bundle: ResultBundle = ResultBundle(
                model_name=endpoint_request.model_name,
                predictions=[
                    prediction.to_dict() for prediction in predictions
                ],
                iteration_publish_name=model.publish_name,
                other_metadata={
                    app_properties.app_name + '_' + endpoint_request.model_name:
                    result
                })
            MetadataUpdater.update_metadata(
                result_bundle=result_bundle,
                image_data=image_data,
                app_properties=app_properties,
                louvre_client=louvre_client,
                plugin_id=endpoint_request.plugin_id)

    @staticmethod
    def _extract_most_likely_category(
            predictions: List[ClassificationPredictionResult],
            probability_threshold: float) -> str:
        """
        Return the most probable category, if its probability is above a threshold value.
        """
        category: Optional[ClassificationPredictionResult] = None

        for prediction in predictions:
            if prediction.probability >= probability_threshold and (
                    category is None
                    or category.probability < prediction.probability):
                category = ClassificationPredictionResult(
                    probability=prediction.probability,
                    tag_name=prediction.tag_name)

        return 'UNDEFINED' if category is None else category.tag_name


class ObjectDetectionPrediction:
    """
    Class with methods to make object detection predictions.
    """
    @staticmethod
    def detect_from_image_data(
        prediction_client: CustomVisionPredictionClient,
        model: Iteration,
        image_data: ImageData,
        probability_threshold: float = 0
    ) -> List[ObjectDetectionPredictionResult]:
        """
        Detect objects on an image and return predictions given a Custom Vision model.

        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param Iteration model: Published Custom Vision iteration
        :param ImageData image_data: Image data from a previous call to ImageAPI
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.

        :rtype: List[ObjectDetectionPredictionResult]
        
        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreVisionValueError:
        :raises RequestException:
        """

        image_entry = ImageMethods.get_image_from_image_data(
            image_data=image_data,
            max_file_size=Config.custom_vision_max_prediction_file_size)
        if image_entry.is_empty:
            raise LouvreImageNotFound()
        predictions: List[Prediction]
        if image_entry.sasuri:
            predictions = prediction_client.detect_image_url_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                url=image_entry.sasuri).predictions
        else:
            predictions = prediction_client.detect_image_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                image_data=image_entry.file_bytes).predictions
        return ObjectDetectionPrediction._extract_predictions_above_threshold(
            predictions=predictions,
            probability_threshold=probability_threshold)

    @staticmethod
    def detect_from_url(
        prediction_client: CustomVisionPredictionClient,
        model: Iteration,
        image_url: str,
        probability_threshold: float = 0
    ) -> List[ObjectDetectionPredictionResult]:
        """
        Return object detection predictions given a model and an image URL.

        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param Iteration model: Published Custom Vision iteration
        :param ImageData image_url: Image URL
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.

        :rtype: List[ObjectDetectionPredictionResult]
        
        :raises CustomVisionErrorException:
        :raises LouvreVisionValueError:
        :raises RequestException:
        """
        # Attempt to find out the image size without actually fetching it
        file_size = Methods.get_remote_file_size(file_url=image_url)
        predictions: List[Prediction]
        if file_size and file_size < Config.custom_vision_max_prediction_file_size:
            predictions = prediction_client.detect_image_url_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                url=image_url).predictions
        else:
            predictions = prediction_client.detect_image_with_no_store(
                project_id=model.project_id,
                published_name=model.publish_name,
                image_data=ImageMethods.resize_from_url(
                    image_url=image_url,
                    image_longer_side=Config.image_longer_side)).predictions
        return ObjectDetectionPrediction._extract_predictions_above_threshold(
            predictions=predictions,
            probability_threshold=probability_threshold)

    @staticmethod
    def detect(
        prediction_client: CustomVisionPredictionClient,
        louvre_client: LouvreClient,
        model: Iteration,
        image_identifier: str,
        using_production_images: bool = False,
        probability_threshold: float = 0
    ) -> List[ObjectDetectionPredictionResult]:
        """
        Return object detection predictions given a model and either an image URL or an ImageId
        
        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param LouvreClient louvre_client: LouvreClient instance with access to the Louvre environment where this image exists.
        :param Iteration model: Published Custom Vision iteration
        :param str image_identifier: Image URL or Louvre ImageId
        :param bool using_production_images: Whether to fetch images from production. Defaults to False.
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.

        :rtype: List[ObjectDetectionPredictionResult]

        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreKeyError:
        :raises LouvreQueryError:
        :raises LouvreVisionValueError:
        :raises RequestException:          
        """
        if Methods.is_string_url(input_str=image_identifier):
            return ObjectDetectionPrediction.detect_from_url(
                prediction_client=prediction_client,
                model=model,
                image_url=image_identifier,
                probability_threshold=probability_threshold)
        image_data = louvre_client.get_image_data(
            image_id=image_identifier,
            using_production_images=using_production_images)
        return ObjectDetectionPrediction.detect_from_image_data(
            prediction_client=prediction_client,
            model=model,
            image_data=image_data,
            probability_threshold=probability_threshold)

    @staticmethod
    def _extract_predictions_above_threshold(
        predictions: List[Prediction],
        probability_threshold: Optional[float] = 0
    ) -> List[ObjectDetectionPredictionResult]:
        """
        Return custom predition result objects given Custom Vision predictions and a cutoff 
        probability threshold (defined in the configuration)
        """
        result = []
        for prediction in predictions:
            if prediction.probability > probability_threshold:
                result.append(
                    ObjectDetectionPredictionResult(
                        probability=prediction.probability,
                        region=ImageRegion(
                            tag_name=prediction.tag_name,
                            bounding_box=ObjectDetectionPrediction.
                            _extract_bounding_box(
                                bounding_box=prediction.bounding_box))))
        return result

    @staticmethod
    def _extract_bounding_box(
            bounding_box: BoundingBox,
            decimal_places: Optional[int] = None) -> RegionBoundingBox:

        if decimal_places is None:
            decimal_places = Config.predictions_rounding_decimal_places
        return RegionBoundingBox(top=round(bounding_box.top, decimal_places),
                                 left=round(bounding_box.left, decimal_places),
                                 width=round(bounding_box.width,
                                             decimal_places),
                                 height=round(bounding_box.height,
                                              decimal_places))

    @staticmethod
    def _is_tag_predicted(predictions: List[PredictionResult], tag_name: str,
                          probability_threshold: float) -> bool:
        for prediction in predictions:
            detected: bool = isinstance(
                prediction, ObjectDetectionPredictionResult
            ) and prediction.probability >= probability_threshold and prediction.region.tag_name == tag_name
            classified: bool = isinstance(
                prediction, ClassificationPredictionResult
            ) and prediction.probability >= probability_threshold and prediction.tag_name == tag_name

            if detected or classified:
                return True

        return False

    @staticmethod
    def detect_tag_and_update_metadata(
            prediction_client: CustomVisionPredictionClient,
            louvre_client: LouvreClient,
            prediction_request: CustomVisionPluginPredictionRequest,
            tag_to_detect: str,
            app_properties: AppProperties,
            single_boolean_entry: bool = False,
            probability_threshold: float = 0) -> None:
        """
        Check if a given tag is detected, then update the image metadata.
        Predictions are not run if a metadata entry already exists. 

        :param CustomVisionPredictionClient prediction_client: Custom Vision prediction client
        :param LouvreClient louvre_client: LouvreClient instance with access to the Louvre environment where this image exists.
        :param CustomVisionPluginPredictionRequest prediction_request: Contains the incoming request and the model.
        :param str tag_to_detect: Name of the tag/category that one wants to detect on the image.
        :param AppProperties app_properties: Object that describes the application.
        :param bool single_boolean_entry: If given, a single *_boolean* metadata tag will be generated, based on all allowed models.
        :param float probability_threshold: Filters out predictions below this probability cutoff value. Defaults to zero.

        :raises CustomVisionErrorException:
        :raises LouvreImageNotFound:
        :raises LouvreKeyError:
        :raises LouvreQueryError:
        :raises LouvreVisionValueError:
        :raises RequestException: 
        """
        image_data = louvre_client.get_image_data(
            image_id=prediction_request.endpoint_request.image_identifier)
        existing_entry = MetadataUpdater.exists(
            image_data=image_data,
            model_name=prediction_request.endpoint_request.model_name,
            app_name=app_properties.app_name,
            app_version=app_properties.app_version,
            iteration_publish_name=prediction_request.model.publish_name)
        if not existing_entry:
            predictions = ObjectDetectionPrediction.detect_from_image_data(
                prediction_client=prediction_client,
                model=prediction_request.model,
                image_data=image_data,
                probability_threshold=probability_threshold)

            boolean_entry = ObjectDetectionPrediction.get_boolean_metadata_entry(
                predictions=predictions,
                image_data=image_data,
                tag_to_detect=tag_to_detect,
                model_name=prediction_request.endpoint_request.model_name,
                single_boolean_entry=single_boolean_entry,
                probability_threshold=probability_threshold,
                app_properties=app_properties)

            result_bundle: ResultBundle = ResultBundle(
                model_name=prediction_request.endpoint_request.model_name,
                predictions=[
                    prediction.to_dict() for prediction in predictions
                ],
                iteration_publish_name=prediction_request.model.publish_name,
                other_metadata=boolean_entry)
            MetadataUpdater.update_metadata(
                result_bundle=result_bundle,
                image_data=image_data,
                app_properties=app_properties,
                louvre_client=louvre_client,
                plugin_id=prediction_request.endpoint_request.plugin_id)

    @staticmethod
    def get_boolean_metadata_entry(
            predictions: List[ObjectDetectionPredictionResult],
            image_data: ImageData, tag_to_detect: str, model_name: str,
            single_boolean_entry: bool, probability_threshold: float,
            app_properties: AppProperties) -> Dict[str, str]:
        """
        Generate a metadata entry with a boolean value depending on the predictions.
        The key depends on whether a list of allowed models is given. If a list of models 
        is given, the result key will be common for all models, i.e. *app_name_boolean*.
        Otherwise, the tag generated will be model-specific, i.e. *app_name_model_name*.

        :param List[ObjectDetectionPredictionResult] predictions: Fresh prediction results
        :param ImageData image_data: ImageData instance corresponding to the current image
        :param str tag_to_detect: Name of the desired tag/category 
        :param str model_name: Model name
        :param bool single_boolean_entry: Whether to generate a single boolean tag based on all allowed models.
        :param float probability_threshold: Filters out predictions below this probability cutoff value.
        :param AppProperties app_properties: Object describing the caller app.
        :rtype: Dict[str, str]
        """

        boolean_key: str = app_properties.app_name + '_' + model_name
        boolean_result = ObjectDetectionPrediction._is_tag_predicted(
            predictions=predictions,
            tag_name=tag_to_detect,
            probability_threshold=probability_threshold)

        if single_boolean_entry:
            boolean_key = app_properties.app_name + '_' + 'boolean'
            existing_entries: List[
                MetadataEntry] = MetadataUpdater._get_package_metadata_entries_from_image_data(
                    image_data=image_data, app_name=app_properties.app_name)
            boolean_existing: bool = False
            for existing in [
                    _ for _ in existing_entries if _.model_name != model_name
            ]:
                if existing.model_name in app_properties.allowed_model_names and ObjectDetectionPrediction._is_tag_predicted(
                        predictions=MetadataUpdater.parse_predictions(
                            predictions=existing.predictions),
                        tag_name=tag_to_detect,
                        probability_threshold=0):
                    boolean_existing = True

            boolean_result = boolean_result or boolean_existing

        return {boolean_key: str(boolean_result)}
