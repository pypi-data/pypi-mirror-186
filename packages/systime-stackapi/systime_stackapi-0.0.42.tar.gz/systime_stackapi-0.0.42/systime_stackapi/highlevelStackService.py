import json
import requests
from .authenticator import Authenticator


class HighlevelStackService(Authenticator):
    def __init__(self, service_url, client_key_id, shared_secret, **kwargs):
        self.service_url = service_url
        self.service_token = 'HighlevelStackService'
        self.timeout = kwargs.get('timeout', 300)
        super().__init__(client_key_id, shared_secret, **kwargs)

    def upload_frontpage_image(self, isbn, image_payload):
        path = '/frontpage-image/{}'.format(isbn)

        files = {'file': ('image.jpg', image_payload)}
        bearer_token = self.get_service_bearer_token(self.service_token)
        r = requests.post(self.service_url + path, files=files, headers={'Authorization': bearer_token},
                          timeout=self.timeout)
        r.raise_for_status()
        return json.loads(r.text)
