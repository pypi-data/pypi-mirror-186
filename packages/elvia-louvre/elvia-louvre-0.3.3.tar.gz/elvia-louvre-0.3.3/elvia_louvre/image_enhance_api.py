from http import HTTPStatus
import json
import requests

from .data_models import UpdateMetadataRequest
from .errors import LouvreQueryError
from .config import Config
from .token import Token


class ImageEnhanceAPI():
    @staticmethod
    def update_metadata(config: Config,
                        update_request: UpdateMetadataRequest) -> None:
        """
        Update image metadata. Existing metadata entries with the same keys will get overwritten.

        :param Config config: Config instance
        :param UpdateMetadataRequest update_request: Metadata update request instance
        :raises errors.LouvreQueryError:
        :raises requests.RequestException:
        """
        payload = {
            "imageID":
            update_request.image_id,
            "additionalMetadataReplaceByKey": [{
                'key': k,
                'value': v
            } for k, v in update_request.additional_metadata.items()],
            "skipValidationOfProvidedETag":
            update_request.skip_e_tag_validation,
            "clientName":
            update_request.client_name
        }

        if update_request.e_tag:
            payload["eTag"] = update_request.e_tag

        if update_request.plugin_id:
            payload["pluginId"] = update_request.plugin_id

        query = json.dumps(payload)

        response = requests.put(url=config.get_secret(
            config.secret_path_sets().get_louvre_domain(False)) +
                                config._image_enhance_api_relative_url,
                                headers=Token.get_headers(config=config),
                                data=query)

        if not response.status_code == HTTPStatus.OK:
            raise LouvreQueryError(response.content)
