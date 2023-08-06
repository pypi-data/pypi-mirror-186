import requests

class WrappedSession(requests.Session):
    def merge_environment_settings(self, url, proxies, stream, verify, *args, **kwargs): ...
