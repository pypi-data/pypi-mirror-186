import json
import re
from urllib.parse import urljoin

from parsel import Selector as _ParselSelector


class SelectorList(_ParselSelector.selectorlist_cls):
    pass


class Selector(_ParselSelector):

    __slots__ = ["response"]
    selectorlist_cls = SelectorList

    def __init__(
        self, response=None, text=None, type=None, root=None, **kwargs
    ):
        if response is not None and text is not None:
            raise ValueError(
                f"{self.__class__.__name__}.__init__() received "
                "both response and text"
            )
        st = "html"
        if text is not None:
            response = Response("", body=text)
        if response is not None:
            text = response.text
            kwargs.setdefault("base_url", response._url)
        self.response = response
        super().__init__(text=text, type=st, root=root, **kwargs)


class Request:
    """
    Represents an HTTP request, which is usually generated in a Spider.
    """

    def __init__(self, url, callback=None, cb_kwargs=None) -> None:
        """
        Represent a http request, that eventually turns into a response.

        ...

        Parameters
        ----------
        url : _type_
            _description_
        callback : _type_, optional
            _description_, by default None
        cb_kwargs : _type_, optional
            _description_, by default None
        """
        self._set_url(url)
        self._callback = callback
        self._cb_kwargs = cb_kwargs

    @property
    def cb_kwargs(self) -> dict:
        """
        Generate callback keyword args for parse functions.

        ...

        Returns
        -------
        dict
            _description_
        """
        if self._cb_kwargs is None:
            self._cb_kwargs = {}
        return self._cb_kwargs

    def _get_url(self) -> str:
        """Return the requests url attribute."""
        return self._url

    def _set_url(self, url: str) -> None:
        """Set the requests url attribute."""
        self._url = url

    @property
    def url(self):
        """Get the requests url attribute."""
        return self._get_url()

    def __repr__(self) -> str:
        """
        Return a string representation of the class instance object.

        Returns
        -------
        str
            description of the class
        """
        return f"<Req {self.url}>"


class Response:
    """
    Represents the response from the http request.
    """

    base_url_pattern = re.compile(
        r"<base\s[^>]*href\s*=\s*[\"\']\s*([^\"\'\s]+)\s*[\"\']", re.I
    )
    comments_pattern = re.compile("<!--.*?(?:-->|$)", re.DOTALL)

    def __init__(self, url, body=None, page=None, browser=None, request=None):
        """Construct the new response object."""
        self._set_url(url)
        self._set_body(body)
        self._page = page
        self._browser = browser
        self._request = request
        self._cached_selector = None

    @property
    def body(self):
        """Return the html content."""
        return self._get_body()

    text = body

    @property
    def url(self):
        """Return the url attribute."""
        return self._get_url()

    def json(self):
        """Return the json content of the body."""
        try:
            data = json.loads(self._body)
            return data
        except json.JSONDecodeError:
            return {}

    @property
    def raw(self):
        """Return the raw bytes from the response body."""
        return self._body.encode("utf-8")

    def urljoin(self, url):
        """Merge the path and base portions of the url."""
        return urljoin(self.url, url)

    @property
    def selector(self):
        """Return the response object as a selector."""
        if self._cached_selector is None:
            self._cached_selector = Selector(self)
        return self._cached_selector

    def xpath(self, query, **kwargs):
        """Parse the html for the specific xpath expression."""
        return self.selector.xpath(query, **kwargs)

    def css(self, query):
        """Parse the html for the css expression."""
        return self.selector.css(query)

    @property
    def request(self):
        return self._request

    @property
    def cb_kwargs(self):
        """Return the callback keyword args for the response."""
        return self.request.cb_kwargs

    def _get_url(self):
        """Return the url attribute."""
        return self._url

    def _set_url(self, url):
        """Return the url attribute."""
        self._url = url

    def _get_body(self):
        """Return the body of the response."""
        return self._body

    def _set_body(self, body):
        """Set the html or json body for the response."""
        if body is None:
            self._body = b""
        else:
            self._body = body

    def __repr__(self):
        """Return the string representation of the class instance."""
        return f"<Resp {self.url}>"
