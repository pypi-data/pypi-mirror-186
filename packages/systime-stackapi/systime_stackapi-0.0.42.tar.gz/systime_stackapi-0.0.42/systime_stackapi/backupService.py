import json

import requests

from .authenticator import Authenticator


class BackupService(Authenticator):
    def __init__(self, service_url, client_key_id, shared_secret, **kwargs):
        self.service_url = service_url
        self.service_token = 'BackupService'
        self.timeout = kwargs.get('timeout', 300)
        super().__init__(client_key_id, shared_secret, **kwargs)

    def request_url(self, path, bearer_token, method='get', data=None):
        headers = {'Content-Type': 'application/json', 'Authorization': bearer_token}
        url = self.service_url + path
        if data is not None:
            data = json.dumps(data)

        r = requests.request(method, url, headers=headers, timeout=self.timeout, data=data)
        r.raise_for_status()
        return r

    def create_signed_upload_links(self, backup_policy, backup_type, backup_name):
        path = '/backups/{}/{}/{}'.format(backup_policy, backup_type, backup_name)
        bearer_token = self.get_service_bearer_token(self.service_token)
        r = self.request_url(path, bearer_token, 'POST')
        return json.loads(r.text)

    def get_signed_download_links(self, backup_policy, backup_type, backup_name, backup_id):
        path = '/backups/{}/{}/{}/{}'.format(backup_policy, backup_type, backup_name, backup_id)
        bearer_token = self.get_service_bearer_token(self.service_token)
        r = self.request_url(path, bearer_token, 'GET')
        return json.loads(r.text)

    def list_backups(self, backup_policy, backup_type):
        path = '/backups/{}/{}'.format(backup_policy, backup_type)
        bearer_token = self.get_service_bearer_token(self.service_token)
        r = self.request_url(path, bearer_token, 'GET')
        return json.loads(r.text)

    def get_backup_encryption_keys(self):
        path = '/backup_encryption/encrypt'
        bearer_token = self.get_service_bearer_token(self.service_token)
        r = self.request_url(path, bearer_token, 'POST')
        return json.loads(r.text)

    def decrypt_kms_data_key(self, kms_datakey_encrypted):
        path = '/backup_encryption/decrypt'
        bearer_token = self.get_service_bearer_token(self.service_token)
        data = {'kms_datakey_encrypted': kms_datakey_encrypted}
        r = self.request_url(path, bearer_token, 'POST', data)
        return json.loads(r.text)
