from datetime import datetime, timedelta
from .errors import LouvreSecretError
from typing import Dict
import requests
from .config import Config


class Token():
    """Class for working with jwt tokens."""

    _tokens: Dict[str, str] = {}
    _expiry: Dict[str, datetime] = {}

    @classmethod
    def get_token(cls,
                  config: Config,
                  using_production_images: bool = False) -> str:
        """
        Return the current token if still valid, else a new one.
        
        :param Config config: Config instance
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False  

        :rtype: str
        :raises errors.LouvreSecretError:
        """
        endpoint: str = config.secret_path_sets().get_token_endpoint(
            using_production_images)
        if not endpoint:
            raise LouvreSecretError()
        # Assume that the token life has ended when time is not smaller than the expiry time 
        # minus the buffer
        if endpoint in cls._tokens.keys() and endpoint in cls._expiry.keys(
        ) and datetime.now() < cls._expiry[endpoint] - timedelta(
                seconds=config.token_buffer_seconds):
            return cls._tokens[endpoint]
        return cls.get_new_token(
            config=config, using_production_images=using_production_images)

    @classmethod
    def get_new_token(cls,
                      config: Config,
                      using_production_images: bool = False) -> str:
        """
        Create and get token for this API to communicate with ImageAPI and ImageEnhanceAPI.
        Assume the expiry time is found by adding expires_in to the time right before 
        triggering the request.

        :param Config config: Config instance        
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False  
        :rtype: str    
        :raises errors.LouvreSecretError:
        """
        tick = datetime.now()
        endpoint: str = config.secret_path_sets().get_token_endpoint(
            using_production_images)

        token_response = requests.post(
            url=config.get_secret(endpoint),
            headers={},
            data={
                'grant_type':
                'client_credentials',
                'client_id':
                config.get_secret(config.secret_path_sets().get_client_id_api(
                    using_production_images)),
                'client_secret':
                config.get_secret(
                    config.secret_path_sets().get_client_secret_api(
                        using_production_images))
            })

        cls._tokens[endpoint] = token_response.json()['access_token']
        cls._expiry[endpoint] = tick + timedelta(
            seconds=int(token_response.json()['expires_in']))
        return cls._tokens[endpoint]

    @classmethod
    def get_headers(cls,
                    config: Config,
                    using_production_images: bool = False) -> dict:
        """
        Return headers to be used in HTTP requests against ImageAPI / ImageEnhanceAPI.
        
        :param Config config: Config instance        
        :param using_production_images: Whether to search in production.
        :type using_production_images: bool, defaults to False  
        :rtype: dict    
        :raises errors.LouvreSecretError:
        """
        return {
            "Authorization":
            "Bearer {}".format(
                cls.get_token(
                    config=config,
                    using_production_images=using_production_images)),
            'Content-Type':
            'application/json'
        }
