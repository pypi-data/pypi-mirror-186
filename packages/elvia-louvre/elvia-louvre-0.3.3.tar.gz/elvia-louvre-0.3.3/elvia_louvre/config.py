from typing import Union

from elvia_vault import VaultClient
from .errors import LouvreVaultConnError, LouvreSecretError
from .data_models import SecretPathSets


class Config():
    """        
    Class that encapsulates configuration and a connection to a vault service.
    When in cluster it uses kubernetes auth, else requires a Github token.

    :param data_models.SecretPathSets secret_path_sets: Contains SecretPathSet objects with necessary secret paths
    :param github_token: Github token
    :type github_token: str, optional

    :raises errors.LouvreVaultConnError:
    """

    _vault: VaultClient
    _secrets: dict = {}
    _secret_path_sets: SecretPathSets

    # ImageAPI - GraphQL API to fetch images
    _image_api_relative_url: str = '/image/graphql'

    # ImageEnhanceAPI - API to update image's metadata
    _image_enhance_api_relative_url: str = '/imageenhance/Metadata'

    # Token buffer in seconds
    token_buffer_seconds: int = 60

    def __init__(self,
                 secret_path_sets: SecretPathSets,
                 github_token: Union[str, None] = None):

        # Clean up, to avoid mixing secrets from different vaults, in the case
        # VAULT_ADDR changes between calls
        self._secrets = {}
        self._secret_path_sets = secret_path_sets
        # Get a fresh VaultClient instance and connect to the vault service
        try:
            self._vault = VaultClient(github_token=github_token)
        except Exception as exception:
            raise LouvreVaultConnError(str(exception))

    def get_secret(self, secret_path: str) -> str:
        """
        Return a secret value given a secret path.
        Fetch from vault only if not previously fetched.

        :param secret_path: Secret Path in the vault
        :type secret_path: str
        
        :rtype: str

        :raises errors.LouvreSecretError:
        """
        try:
            if not secret_path in self._secrets.keys():
                self._secrets[secret_path] = self._vault.get_value(secret_path)
            return self._secrets[secret_path]

        except KeyError as exception:
            raise LouvreSecretError(exception)

    def secret_path_sets(self) -> SecretPathSets:
        """
        Return the SecretPathSets object with which the client was initialised.
        
        :rtype: SecretPathSets
        :raises errors.LouvreSecretError:
        """
        if '_secret_path_sets' in vars(self):
            return self._secret_path_sets
        raise LouvreSecretError()
