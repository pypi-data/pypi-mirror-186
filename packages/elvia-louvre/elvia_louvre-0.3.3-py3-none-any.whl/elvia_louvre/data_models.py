from dataclasses import dataclass, field
from elvia_louvre.errors import LouvreSecretError
from typing import Dict, List, Optional, Union


@dataclass
class ImageFile:
    """
    Represent image files from ImageAPI.
    
    :param str image_variant: Name of the image variant for this file
    :param int size: File size in bytes.
    :param str sasuri: URL to the file. It contains a token with built-in expiring access to the resource.
    :param float height: Image height in pixels.
    :param float width: Image width in pixels.
    """

    image_variant: str
    size: int
    sasuri: str
    height: float
    width: float


@dataclass
class ImageData:
    """
    Represent image data from ImageAPI.
    
    :param str image_id:
    :param str etag:
    :param List[dict] metadata:
    :param List[data_models.ImageFile] image_files:
    """

    image_id: str
    etag: str
    metadata: List[dict]
    image_files: List[ImageFile]

    @property
    def image_variants(self) -> List[str]:
        """
        Return a list with the imageVariants present.

        :rtype: List[str]
        """
        return [image_file.image_variant for image_file in self.image_files]

    def get_variant(self, variant: str) -> Union[ImageFile, None]:
        """
        Given an image variant, return its corresponding ImageFile if it exits in the ImageData 
        instance.

        :param variant: Name of the desired image variant.
        :type variant: str            

        :rtype: data_models.ImageFile, optional
        """
        for image_file in self.image_files:
            if variant == image_file.image_variant:
                return image_file
        return None


@dataclass
class UpdateMetadataRequest:
    """
    Represent a metadata update request to be sent to ImageEnhanceAPI.
    
    :param str image_id: Image identifier in the Louvre system
    :param additional_metadata: Dictionary with the metadata entries to be updated
    :type additional_metadata: Dict[str, str], defaults to {}
    :param plugin_id: Plugin identifier
    :type plugin_id: str, optional
    :param e_tag: Concurrency tag
    :type e_tag: str, optional
    :param bool skip_e_tag_validation: Whether to skip concurrency tag validation
    :type skip_e_tag_validation: bool, defaults to True
    :param client_name: Client name
    :type client_name: str, defaults to python-client
    
    """

    image_id: str
    additional_metadata: Dict[str, str] = field(default_factory=dict)
    plugin_id: Optional[str] = None
    e_tag: Optional[str] = None
    skip_e_tag_validation: bool = True
    client_name: str = 'python-client'


@dataclass
class SecretPathSet:
    """
    Store secret paths
    
    :param str LOUVRE_DOMAIN: Secret path for the Louvre domain
    :param str TOKEN_ENDPOINT: Secret path for the ElvID token endpoint
    :param str CLIENT_ID_API: Secret path for the client id 
    :param str CLIENT_SECRET_API: Secret path for the client secret
    """
    LOUVRE_DOMAIN: str
    TOKEN_ENDPOINT: str
    CLIENT_ID_API: str
    CLIENT_SECRET_API: str


@dataclass
class SecretPathSets:
    """
    Store sets of secret paths

    :param SecretPathSet secret_path_set: Secret paths to be used
    :param secret_path_set_prod: Secret paths against production
    :type secret_path_set_prod: SecretPathSet, optional
    """
    secret_path_set: SecretPathSet
    secret_path_set_prod: Optional[SecretPathSet] = None

    def get_louvre_domain(self, using_production_images: bool = False) -> str:
        """
        Return the louvre domain secret path.

        :param using_production_images: If the production value is desired.
        :type using_production_images: bool, defaults to False
        :raises errors.LouvreSecretError:
        """
        if not using_production_images:
            return self.secret_path_set.LOUVRE_DOMAIN
        if using_production_images and self.secret_path_set_prod:
            return self.secret_path_set_prod.LOUVRE_DOMAIN
        raise LouvreSecretError()

    def get_token_endpoint(self, using_production_images: bool = False) -> str:
        """
        Return the token endpoint secret path.

        :param using_production_images: If the production value is desired.
        :type using_production_images: bool, defaults to False
        :raises errors.LouvreSecretError:
        """        
        if not using_production_images:
            return self.secret_path_set.TOKEN_ENDPOINT
        if using_production_images and self.secret_path_set_prod:
            return self.secret_path_set_prod.TOKEN_ENDPOINT
        raise LouvreSecretError()

    def get_client_id_api(self, using_production_images: bool = False) -> str:
        """
        Return the client id api secret path.

        :param using_production_images: If the production value is desired.
        :type using_production_images: bool, defaults to False
        :raises errors.LouvreSecretError:
        """           
        if not using_production_images:
            return self.secret_path_set.CLIENT_ID_API
        if using_production_images and self.secret_path_set_prod:
            return self.secret_path_set_prod.CLIENT_ID_API
        raise LouvreSecretError()

    def get_client_secret_api(self,
                              using_production_images: bool = False) -> str:
        """
        Return the client secret api secret path.

        :param using_production_images: If the production value is desired.
        :type using_production_images: bool, defaults to False
        :raises errors.LouvreSecretError:
        """                                 
        if not using_production_images:
            return self.secret_path_set.CLIENT_SECRET_API
        if using_production_images and self.secret_path_set_prod:
            return self.secret_path_set_prod.CLIENT_SECRET_API
        raise LouvreSecretError()
