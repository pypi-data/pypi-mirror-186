from http import HTTPStatus
import requests
from typing import Dict, Union, List

from .config import Config
from .data_models import ImageData, ImageFile
from .enums import ImageVariants
from .errors import LouvreImageNotFound, LouvreQueryError, LouvreKeyError, \
    LouvreInvalidImageVariant
from .token import Token


class ImageAPI():
    """Wrapper class for communicating with ImageAPI."""
    @staticmethod
    def get_image_data(config: Config,
                       img_id: str,
                       using_production_images: bool = False) -> ImageData:
        """
        Return image data for a given image ID.

        :param Config config: Config instance.
        :param str img_id: ID of the image.
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False

        :rtype: ImageData

        :raises errors.LouvreImageNotFound:
        :raises errors.LouvreKeyError:
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """

        query = \
            f'''query GetImage {{
                    getImage(id: "{img_id}")
                    {{
                        _etag
                        additionalMetadata {{
                            key
                            value          
                        }}
                        imageFiles {{
                            imageVariant
                            sasUri
                            size
                            height
                            width
                        }}                        
                    }}
                }}'''

        response = requests.post(
            url=config.get_secret(config.secret_path_sets().get_louvre_domain(
                using_production_images)) + config._image_api_relative_url,
            json={'query': query},
            headers=Token.get_headers(
                config=config,
                using_production_images=using_production_images))

        if response.status_code == HTTPStatus.OK:
            try:
                return ImageData(
                    image_id=img_id,
                    etag=response.json()['data']['getImage']['_etag'],
                    image_files=ImageAPI._extract_image_files(
                        image_files=response.json()['data']['getImage']
                        ['imageFiles']),
                    metadata=ImageAPI._extract_additional_metadata(
                        metadata=response.json()['data']['getImage']
                        ['additionalMetadata']))
            except KeyError as key_error:
                raise LouvreKeyError(str(key_error))
        elif response.status_code == HTTPStatus.BAD_REQUEST and 'No image with id' in str(
                response.content):
            raise LouvreImageNotFound()
        raise LouvreQueryError(
            str(response.status_code) + '\n' + response.text)

    @staticmethod
    def get_image_sasuri(config: Config,
                         img_id: str,
                         image_variant: Union[str, None] = None,
                         using_production_images: bool = False) -> str:
        """
        Given image ID and image variant, return the corresponding sasuri.

        :param Config config: Config instance.
        :param str img_id: ID of the image.
        :param image_variant: Image size. Valid choices are thumbnail, standard and original.
        :type image_variant: str, optional            
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False           
            
        :returns: Link to the desired image file with a built-in expiring access token.
        :rtype: str

        :raises errors.LouvreImageNotFound:
        :raises errors.LouvreKeyError:
        :raises errors.LouvreQueryError:
        :raises errors.LouvreInvalidImageVariant:
        :raises requests.RequestException:
        """

        if image_variant is None:
            image_variant = ImageVariants.DEFAULT
        if image_variant not in [
                ImageVariants.THUMBNAIL, ImageVariants.STANDARD,
                ImageVariants.ORIGINAL
        ]:
            raise LouvreInvalidImageVariant()

        query = \
            f'''query GetImage {{
                    getImage(id: "{img_id}", imageVariants: ["{image_variant}"]) {{
                        imageFiles {{
                            sasUri
                        }}
                    }}
                }}'''

        response = requests.post(
            url=config.get_secret(config.secret_path_sets().get_louvre_domain(
                using_production_images)) + config._image_api_relative_url,
            json={'query': query},
            headers=Token.get_headers(
                config=config,
                using_production_images=using_production_images))

        if response.status_code == 200:
            try:
                return response.json(
                )['data']['getImage']['imageFiles'][0]['sasUri']
            except KeyError as key_error:
                raise LouvreKeyError(str(key_error))
        elif response.status_code == HTTPStatus.BAD_REQUEST and 'No image with id' in str(
                response.content):
            raise LouvreImageNotFound()
        else:
            raise LouvreQueryError(
                str(response.status_code) + '\n' + response.text)

    @staticmethod
    def _extract_image_files(image_files: list) -> List[ImageFile]:
        result = []
        if isinstance(image_files, list):
            for image_file in image_files:
                if isinstance(image_file, dict) and all([
                        key in image_file.keys() for key in
                    ['imageVariant', 'size', 'sasUri', 'height', 'width']
                ]):
                    result.append(
                        ImageFile(image_variant=str(
                            image_file['imageVariant']),
                                  size=int(image_file['size']),
                                  sasuri=str(image_file['sasUri']),
                                  height=float(image_file['height']),
                                  width=float(image_file['width'])))
        return result

    @staticmethod
    def _extract_additional_metadata(
            metadata: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Return a list of dictionaries, each with the original key name and their corresponding values, 
        without deserialising."""
        result: List[Dict[str, str]] = []
        if not isinstance(metadata, list):
            return []
        for item in metadata:
            if not isinstance(item, dict) or not 'key' in item.keys(
            ) or not 'value' in item.keys():
                continue
            result.append({item['key']: item['value']})
        return result
