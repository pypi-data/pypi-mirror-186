import types
import typing
import functools

from .__log import logger

class ProxyProvider:
    def __init__(self, origin: types.MethodType) -> None:
        self.origin = origin
    def __init_requests__(self) -> typing.Self:
        import requests
        self.requests = requests
        return self
    def __init__urlopen__(self) -> typing.Self:
        import urllib
        import urllib.parse
        import urllib.request
        self.urllib = urllib
        self.urllib_parse = urllib.parse
        self.urllib_request = urllib.request
        return self
    def urlopen(self, url, *args, **kwargs) -> typing.Any:
        logger.info("Proxy urllib.request.urlopen by {}".format(self.__class__.__name__))
        return self.with_urlopen(url, *args, **kwargs)
    def request(self, url, *args, **kwargs) -> typing.Any:
        logger.info("Proxy requests.request by {}".format(self.__class__.__name__))
        return self.with_requests(url, *args, **kwargs)
    def with_urlopen(self, url, *args, **kwargs) -> typing.Any: pass
    def with_requests(self, url, *args, **kwargs) -> typing.Any: pass

class ProxySite(ProxyProvider):
    proxy_url = "https://us7.proxysite.com/includes/process.php?action=update"
    def with_requests(self, url, *args, **kwargs) -> typing.Any:
        return self.requests.post(self.proxy_url, {
            "d": url
        }, *args, **kwargs)
    def with_urlopen(self, url, *args, **kwargs) -> typing.Any:
        return self.origin(self.proxy_url, self.urllib_parse.urlencode({
            "d": url
        }).encode())

def request(provider: type[ProxyProvider], origin: types.MethodType, url: str, *args, **kwargs) -> typing.Any:
    return provider(origin).__init_requests__().request(url, *args, **kwargs)

def urlopen(provider: type[ProxyProvider], origin: types.MethodType, url: str, *args, **kwargs) -> typing.Any:
    return provider(origin).__init__urlopen__().urlopen(url, *args, **kwargs)

def proxy(module: types.ModuleType, provider: type[ProxyProvider]=ProxySite) -> None:
    if module.__name__ == "requests":
        module.get = functools.partial(request, provider, module.get)
    elif module.__name__ == "urllib.request":
        module.urlopen = functools.partial(urlopen, provider, module.urlopen)
    else:
        logger.warning("Unsupported http client")