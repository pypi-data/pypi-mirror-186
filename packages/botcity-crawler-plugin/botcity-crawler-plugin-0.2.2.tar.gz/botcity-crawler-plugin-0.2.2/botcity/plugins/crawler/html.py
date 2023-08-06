from typing import Any, List

import requests_html


class HTML:

    def __init__(self, html: requests_html.HTML, javascript_enabled: bool = False) -> None:
        """HTML representation of a page.

        Args:
            html (requests_html.HTML): the page html object from `requests_html`.
            javascript_enabled (bool): Whether or not JavaScript was enabled for this request. Defaults to False.
        """
        self._javascript_enabled = javascript_enabled
        self.page = html
        self.current = self.page.find("html", first=True)

    def query_selector(self, selectors: str, reset: bool = False):
        """
        Searches the first element within the document which matches the specified
        group of selectors.

        Args:
            selectors (str): One or more selectors
            reset (bool): Whether or not to reset the current element before the search.

        Returns:
            HTML: this object
        """
        if reset:
            self.reset()
        self.current = self.current.find(selectors, first=True)
        return self

    def query_selector_all_size(self, selectors: str, reset: bool = False) -> int:
        """Searches all elements within the document which matches the specified
        group of selectors and return the number of elements.

        Args:
            selectors (str): One or more selectors
            reset (bool): Whether or not to reset the current element before the search.

        Returns:
            int: number of elements
        """
        if reset:
            self.reset()
        return len(self.current.find(selectors))

    def query_selector_iter_all(self, selectors: str, reset: bool = False):
        """Searches all elements within the document which matches the specified
        group of selectors and iterate over the results setting the `current` element.

        Args:
            selectors (str): One or more selectors
            reset (bool): Whether or not to reset the current element before the search.

        Returns:
            HTML: this object
        """
        if reset:
            self.reset()
        elems = self.current.find(selectors)
        for el in elems:
            self.current = el
            yield self

    def query_selector_all(self, selectors: str, index: int, reset: bool = False):
        """Searches all elements within the document which matches the specified
        group of selectors and returns the specified index.

        Args:
            selectors (str): One or more selectors
            index (int): The index of the element of the list
            reset (bool): Whether or not to reset the current element before the search.

        Returns:
            HTML: this object
        """
        if reset:
            self.reset()
        self.current = self.current.find(selectors)[index]
        return self

    def reset(self):
        """Reset the current element to the top of the page.
        """
        self.current = self.page.find("HTML", first=True)
        return self

    def get_element_by_id(self, id: str):
        """
        Searches the element within the document which matches the id.

        Args:
            id (str): Unique identifier of the element.
        """
        self.current = self.page.xpath(
            "//*[@id=\"{}\"]".format(id), first=True)
        return self

    def execute_javascript(self, code: str) -> Any:
        """Executes the specified JavaScript code within the page.

        The usage would be similar to what can be achieved when executing
        JavaScript in the current page by entering "javascript:...some JS code..."
        in the URL field of a browser.

        If JavaScript was not enabled on the Plugin before the request, calls
        to this method will be ignored.

        Args:
            code (str): the JavaScript code to be executed.
        """
        if not self._javascript_enabled:
            return None
        return self.page.render(script=code, reload=False)

    def get_attribute(self, attribute) -> Any:
        """Returns the value of the attribute in an element.

        Args:
            attribute (str): The attribute name of element.

        Raises:
            RuntimeError: If the element has no attributes.
            KeyError: [description]

        Returns:
            object: The attribute value.
        """
        if not self.current.attrs:
            raise RuntimeError("The element doesn't have attributes.")
        if attribute not in self.current.attrs:
            raise KeyError(
                f"The element doesn't have an attribute with the name '{attribute}'.")

        return self.current.attrs.get(attribute)

    def value(self) -> Any:
        """Returns the value of an element.

        Returns:
            str: The element value.
        """
        if self.current:
            return self.current.text
        return None

    def elements(self) -> List:
        """Returns all child elements.

        Returns:
            List of elements.
        """
        return self.current.find()
