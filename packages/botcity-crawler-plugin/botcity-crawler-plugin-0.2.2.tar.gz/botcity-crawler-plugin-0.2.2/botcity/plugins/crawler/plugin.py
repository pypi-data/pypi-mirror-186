from requests_html import HTMLSession

from .html import HTML


class BotCrawlerPlugin:
    def __init__(self, javascript_enabled=False) -> None:
        """
        BotCrawlerPlugin

        Args:
            javascript_enabled (bool, optional): Whether or not JavaScript should be enabled
                when making requests. Defaults to False.
        """
        # verify controls whether or not we verify SSL certificates
        # by default we don't
        self.session = HTMLSession(verify=False)
        self._css_enabled = False
        self._javascript_enabled = javascript_enabled

    @property
    def javascript_enabled(self) -> bool:
        """Whether or not JavaScript should be enabled when making
        the request.
        """
        return self._javascript_enabled

    @javascript_enabled.setter
    def javascript_enabled(self, enable: bool) -> None:
        self._javascript_enabled = enable

    def request(self, url: str, wait_time: int = 0):
        """Executes a request to the given URL

        Args:
            url (str): The desired URL.
            wait_time (int): The number of milliseconds to wait after initial render.

        Returns:
            HTML: an HTML object which can be used to parse elements.
                See [HTML][botcity.plugins.crawler.html.HTML]
        """
        response = self.session.get(url)
        if self.javascript_enabled:
            response.html.render(sleep=wait_time/1000)
        return HTML(response.html, self.javascript_enabled)

    def request_as_string(self, url: str) -> str:
        return self.request(url).html.text
