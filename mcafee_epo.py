import json
from requests import Session

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class APIException(Exception):
    pass


class Client:
    def __init__(self, url, username, password, session=None):
        self.url = url
        self.username = username
        self.password = password

        if session is None:
            session = Session()

        self._session = session
        self._token = None

    def _get_token(self, _skip=False):
        if self._token is None and not _skip:
            self._token = self._request('core.getSecurityToken', _skip_token=True)

        return self._token

    def _request(self, name, _skip_token=False, **kwargs):
        kwargs.setdefault('auth', (self.username, self.password))
        params = kwargs.setdefault('params', {})
        params.setdefault(':output', 'json')
        params.setdefault('orion.user.security.token', self._get_token(_skip=_skip_token))
        url = urljoin(self.url, 'remote/{}'.format(name))

        if kwargs.get('data') or kwargs.get('json') or kwargs.get('files'):
            r = self._session.post(url, **kwargs)
        else:
            r = self._session.get(url, **kwargs)

        r.raise_for_status()
        text = r.text

        if not text.startswith('OK:'):
            raise APIException(text)

        return json.loads(text[3:])

    def __call__(self, name, *args, params=None, files=None, **kwargs):
        if params is None:
            params = {}

        for i, item in enumerate(args):
            params['param{}'.format(i)] = item

        params.update(kwargs)
        return self._request(name, params=params, files=files)
