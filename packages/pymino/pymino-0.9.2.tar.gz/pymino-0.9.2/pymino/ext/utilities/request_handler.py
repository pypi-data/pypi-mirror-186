from .generate import *

class RequestHandler:
    """A class that handles all requests"""
    def __init__(self, bot, session: HTTPClient, proxy: Optional[str] = None):
        self.bot            = bot
        self.sid:           Optional[str] = None
        self.userId:        Optional[str] = None
        self.session:       HTTPClient = session
        self.proxy:         dict = {"http": proxy,"https": proxy} if proxy is not None else None

    def service_url(self, url: str) -> str:
        return f"https://service.aminoapps.com/api/v1{url}"
    
    def service_headers(self) -> dict:
        return {
            "NDCLANG": "en",
            "ACCEPT-LANGUAGE": "en-US",
            "USER-AGENT": "Apple iPhone13,4 iOS v15.6.1 Main/3.12.9",
            "HOST": "service.aminoapps.com",
            "CONNECTION": "Keep-Alive",
            "ACCEPT-ENCODING": "gzip, deflate, br",
            "NDCAUTH": f"sid={self.sid}",
            "AUID": self.userId
            }

    def fetch_request(self, method: str) -> Callable:
        request_methods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "DELETE": self.session.delete,
            }
        return request_methods[method]

    def handler(
        self,
        method: str,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
    ) -> dict:

        url, headers, data = self.service_handler(url, data, content_type)
        if all([method=="POST", data is None]):
            headers["CONTENT-TYPE"] = "application/octet-stream"
        
        try:
            response: HTTPResponse = self.fetch_request(method)(
                url, data=data, headers=headers, proxies=self.proxy
            )
        except (
            ConnectionError,
            ReadTimeout,
            SSLError,
            ProxyError,
            ConnectTimeout,
        ):
            self.handler(method, url, data, content_type)

        self.print_response(response)
        return self.handle_response(response)

    def service_handler(
        self,
        url: str,
        data: Union[dict, bytes, None] = None,
        content_type: Optional[str] = None
    ) -> Tuple[str, dict, Union[dict, bytes, None]]:

        service_url = self.service_url(url)
        
        headers = {"NDCDEVICEID": device_id(), **self.service_headers()}

        if data or content_type:
            headers, data = self.fetch_signature(data, headers, content_type)

        return service_url, headers, self.ensure_utf8(data)

    def ensure_utf8(self, data: Union[dict, bytes, None]) -> Union[dict, bytes, None]:
        if data is None: return data

        def handle_dict(data: dict):
            return {key: self.ensure_utf8(value) for key, value in data.items()}

        def handle_str(data: str):
            return data.encode("utf-8")

        handlers = {
            dict: handle_dict,
            str: handle_str
        }

        return handlers.get(type(data), lambda x: x)(data)

    def fetch_signature(
        self,
        data: Union[dict, bytes, None],
        headers: dict,
        content_type: str = None
    ) -> Tuple[dict, Union[dict, bytes, None]]:

        if not isinstance(data, bytes):
            data = dumps(data)

        headers.update({
            "CONTENT-LENGTH": f"{len(data)}",
            "CONTENT-TYPE": content_type or "application/json; charset=utf-8",
            "NDC-MSG-SIG": (
                generate_signature(data)
            ),
        })
        return headers, data

    def handle_response(self, response: HTTPResponse) -> dict:
        if response.status_code != 200:
            with suppress(Exception):
                _response: dict = loads(response.text)
                # TODO: Handle exceptions.
                if _response.get("api:statuscode") == 105:
                    return self.bot.run(self.email, self.password)

            raise Exception(response.text)
            
        return loads(response.text)

    def print_response(self, response: HTTPResponse) -> None:
        if self.bot.debug:
            print(f"{Fore.BLUE}{Style.BRIGHT}{response.request.method}:{Style.RESET_ALL} {response.url}")

    def print_status(self, message: str, status: str = "warning") -> None:
        if status == "warning":
            print(f"{Fore.YELLOW}{Style.BRIGHT}WARNING:{Style.RESET_ALL} {message}")
        elif status == "success":
            print(f"{Fore.GREEN}{Style.BRIGHT}SUCCESS:{Style.RESET_ALL} {message}")
        elif status == "error":
            print(f"{Fore.RED}{Style.BRIGHT}ERROR:{Style.RESET_ALL} {message}")
