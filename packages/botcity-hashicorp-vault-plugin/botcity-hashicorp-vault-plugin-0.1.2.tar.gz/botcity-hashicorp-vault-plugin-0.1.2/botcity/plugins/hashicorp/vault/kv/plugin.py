import posixpath
from typing import Dict, List, Optional

import hvac
from hvac import exceptions


class BotHashicorpKVPlugin:
    def __init__(self, url: str, token: str, namespace: str, mount_point: Optional[str] = None,
                 base_path: Optional[str] = "", **kwargs) -> None:
        """
        BotHashicorpKVPlugin

        [See documentation](https://hvac.readthedocs.io/en/stable/overview.html#getting-started)

        Args:
            url (str): Base URL for the Vault instance being addressed.
            token (str): Authentication token to include in requests sent to Vault.
            namespace (str): Vault Namespace.
            mount_point (str, optional): The "path" the secret engine was mounted on.
            base_path (str, optional): The base path of the secrets.
        """
        self._client = hvac.Client(
            url=url,
            token=token,
            namespace=namespace,
            **kwargs
        )
        self._mount_point = mount_point
        self._base_path = base_path

        if not self._client.is_authenticated():
            raise exceptions.Unauthorized("Unable to authenticate to the Vault service.")

    @property
    def mount_point(self) -> str:
        """
        Returns:
            mount_point: The "path" the secret engine was mounted on.
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, new_mount_point: str):
        """
        Args:
            new_mount_point (str): The "path" the secret engine was mounted on.
        """
        self._mount_point = new_mount_point

    @property
    def base_path(self) -> str:
        """
        Returns:
            base_path: The base path of secret.
        """
        return self._base_path

    @base_path.setter
    def base_path(self, new_base_path: str):
        """
        Args:
            new_base_path (str): The new base path.
        """
        self._base_path = new_base_path

    @property
    def vault_client(self):
        """
        Returns:
            client: hvac instance.
        """
        return self._client

    def create_or_update_secret(self, secret: Dict, path: Optional[str] = "",
                                mount_point: Optional[str] = None, **kwargs) -> Dict:
        """
        Create a new version of a secret at the specified location.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#create-update-secret)
        
        Info:
            This method works with KV version 1 and 2.

        Args:
            secret (str): The contents of the "secret" dict will be stored and returned on read.
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secret_info: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.create_or_update_secret(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point,
            secret=secret,
            **kwargs
        )

    def get_secret_value(self, path: Optional[str] = "", mount_point: Optional[str] = None,
                         version: Optional[int] = None) -> Dict:
        """
        Retrieve the secret value at the specified location.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#read-secret-versions)

        Info:
            This method works with KV version 1 and 2.

        Args:
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.
            version (str, optional): Specifies the version to return. If not set the latest version is returned.

        Returns:
            secret_value: The dict value of secret.
        """  # noqa
        return self._client.secrets.kv.v2.read_secret_version(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point,
            version=version
        )['data']

    def get_secret_metadata(self, path: Optional[str] = "", mount_point: Optional[str] = None) -> Dict:
        """
        Retrieve the secret value at the specified location.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#read-secret-metadata)

        Warning:
            This method only works with KV version 2.

        Args:
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secret_info: The dict metadata of secret.
        """  # noqa
        return self._client.secrets.kv.v2.read_secret_metadata(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point
        )

    def list_secrets(self, path: Optional[str] = "", mount_point: Optional[str] = None) -> List[str]:
        """
        Return a list of key names at the specified location.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#list-secrets)

        Warning:
            This method only works with KV version 2.

        Args:
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secrets: The list of secrets.
        """
        return self._client.secrets.kv.v2.list_secrets(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point
        )['data']['keys']

    def _mark_as_delete_latest_version_of_secret(self, path: str, mount_point: str):
        """
        Mark as delete the latest version of secret.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#delete-latest-version-of-secret)

        Warning:
            This method only works with KV version 2.

        Args:
            path (str): Specifies the path of the secret.
            mount_point (str): The "path" the secret engine was mounted on.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.delete_latest_version_of_secret(
            path=path,
            mount_point=mount_point
        )

    def _mark_as_delete_versions_of_secret(self, path: str, versions: List[int], mount_point: str):
        """
        Mark as delete the specified versions of secret.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#delete-secret-versions)

        Warning:
            This method only works with KV version 2.

        Args:
            path (str): Specifies the path of the secret.
            mount_point (str): The "path" the secret engine was mounted on.
            versions (list): The versions to be deleted. The versioned data will not be deleted, but it will no longer be
                returned in normal get requests.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.delete_secret_versions(
            path=path,
            mount_point=mount_point,
            versions=versions
        )

    def mark_secrets_as_delete(self, path: Optional[str] = "", mount_point: Optional[str] = None,
                               versions: List[int] = None):
        """
        Mark as delete the specified versions of secret.

        Warning:
            This method only works with KV version 2.

        Args:
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.
            versions (list, optional): The versions to be deleted. The versioned data will not be deleted, but it will no longer be
                returned in normal get requests.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        if not versions:
            return self._mark_as_delete_latest_version_of_secret(
                path=posixpath.join(self.base_path, path),
                mount_point=mount_point or self._mount_point
            )
        return self._mark_as_delete_versions_of_secret(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point,
            versions=versions
        )

    def undelete_secrets(self, versions: List[int], path: Optional[str] = "", mount_point: Optional[str] = None):
        """
        This restores the data, allowing it to be returned on get requests.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#undelete-secret-versions)

        Warning:
            This method only works with KV version 2.

        Args:
            versions (list): The versions to be deleted. The versioned data will not be deleted, but it will no longer be
                returned in normal get requests.
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.undelete_secret_versions(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point,
            versions=versions
        )

    def destroy_secret_versions(self, versions: List[int], path: Optional[str] = "",
                                mount_point: Optional[str] = None):
        """
        Permanently remove the specified version.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#destroy-secret-versions)

        Warning:
            This method only works with KV version 2.

        Args:
            versions (list): The versions to be destroyed.
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.destroy_secret_versions(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point,
            versions=versions
        )

    def delete_secret_permanently(self, path: Optional[str] = "", mount_point: Optional[str] = None):
        """
        Delete (permanently) the key metadata and all version data for the specified key.

        [See documentation](https://hvac.readthedocs.io/en/stable/usage/secrets_engines/kv_v2.html#delete-metadata-and-all-versions)

        Warning:
            This method only works with KV version 2.

        Args:
            path (str, optional): Specifies the path of the secret.
            mount_point (str, optional): The "path" the secret engine was mounted on.

        Returns:
            secrets: The dict response of the request.
        """  # noqa
        return self._client.secrets.kv.v2.delete_metadata_and_all_versions(
            path=posixpath.join(self.base_path, path),
            mount_point=mount_point or self._mount_point
        )

    def __setitem__(self, key, value):
        self.create_or_update_secret(path=key, secret=value, mount_point=self._mount_point)

    def __getitem__(self, item):
        return self.get_secret_value(path=item, mount_point=self._mount_point)

    def __delitem__(self, key):
        self.mark_secrets_as_delete(path=key, mount_point=self._mount_point)
