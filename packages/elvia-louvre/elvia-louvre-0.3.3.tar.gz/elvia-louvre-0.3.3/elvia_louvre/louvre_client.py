from elvia_louvre.data_models import SecretPathSets, UpdateMetadataRequest
from elvia_louvre.token import Token
from io import BytesIO
from PIL import Image
import requests

from .config import Config
from .enums import ImageVariants
from .image_api import ImageAPI
from .image_enhance_api import ImageEnhanceAPI


class LouvreClient:
    """
    Python client to interact with APIs in the Louvre system.
    
    :param SecretPathSets secret_path_sets: SecretPathSets instance
    """

    _config: Config
    def __init__(self, secret_path_sets: SecretPathSets):
        self._config = Config(secret_path_sets=secret_path_sets)

    def get_image_data(self,
                       image_id: str,
                       using_production_images: bool = False):
        """
        Return an object with image metadata retrieved from ImageAPI.
        
        :param str image_id: ID of the image.
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False

        :rtype: ImageData
        :raises errors.LouvreImageNotFound:
        :raises errors.LouvreKeyError:
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """
        return ImageAPI.get_image_data(
            config=self._config,
            img_id=image_id,
            using_production_images=using_production_images)

    def get_image_url(self,
                      image_id: str,
                      image_variant: str = ImageVariants.DEFAULT,
                      using_production_images: bool = False) -> str:
        """
        Return the URL of an image variant.

        :param str image_id:  ID of the image.
        :param str image_variant: Accepted values can be found in the ImageVariants class.
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False        

        :rtype: str
        :raises errors.LouvreImageNotFound:
        :raises errors.LouvreInvalidImageVariant:
        :raises errors.LouvreKeyError:
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """
        return ImageAPI.get_image_sasuri(
            config=self._config,
            img_id=image_id,
            image_variant=image_variant,
            using_production_images=using_production_images)

    def get_image(self,
                  image_id: str,
                  image_variant: str = ImageVariants.DEFAULT,
                  using_production_images: bool = False) -> Image:
        """
        Return the image, as a PIL object.

        :param str image_id:  ID of the image.
        :param str image_variant: Accepted values can be found in the ImageVariants class.
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False   

        :returns: PIL.Image
        :raises errors.LouvreImageNotFound:
        :raises errors.LouvreInvalidImageVariant:
        :raises errors.LouvreKeyError:
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """
        file_url = self.get_image_url(
            image_id=image_id,
            image_variant=image_variant,
            using_production_images=using_production_images)
        _response = requests.get(url=file_url)
        _file_bytes = BytesIO(_response.content)
        return Image.open(_file_bytes)

    def update_image_metadata(self,
                              update_request: UpdateMetadataRequest) -> None:
        """
        Update the metadata for an image.

        :param UpdateMetadataRequest update_request: Metadata update request instance
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """
        ImageEnhanceAPI.update_metadata(config=self._config,
                                        update_request=update_request)

    def get_headers(self, using_production_images: bool = False) -> dict:
        """
        Return request headers to be included in a call to Louvre APIs.

        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False    
        :rtype: dict
        :raises errors.LouvreSecretError:
        """
        return Token.get_headers(
            config=self._config,
            using_production_images=using_production_images)
