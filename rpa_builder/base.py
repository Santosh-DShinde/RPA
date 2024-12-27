import time
from typing import Optional, List
from RPA.Browser.Selenium import Selenium
from selenium.webdriver.remote.webelement import WebElement

class RPABuilder:
    """
    A utility class to simplify web automation using the RPA Framework's Selenium library.

    This class provides convenient methods for common browser interactions, such as opening a browser,
    finding elements, entering text, clicking elements, and taking screenshots. It also includes
    handling for implicit waits and improved error reporting.
    """

    def __init__(self, browser: Selenium):
        """
        Initializes the RPABuilder with a Selenium browser instance.
        Args:
            browser: The Selenium browser instance from RPA.Browser.Selenium.
        """
        self.browser = browser

    def open_browser(self, url: str):
        """
        Opens a browser to the specified URL.
        Args:
            url: The URL to open.
        Raises:
            Exception: If there is an error opening the browser.
        """
        try:
            self.browser.open_available_browser(url)
        except Exception as e:
            raise Exception(f"Failed to open browser: {e}")

    def find_element(self, locator: str, timeout: int = 15) -> WebElement:
        """
        Finds a single web element using the given locator. Waits until the element is visible.
        Args:
            locator: The locator for the element (e.g., "id:my-element", "css:.my-class").
            timeout: The maximum time to wait for the element to become visible (in seconds).
        Returns:
            The found WebElement object.
        Raises:
            Exception: If the element is not found within the timeout.
        """
        try:
            self.browser.wait_until_element_is_visible(locator, timeout=timeout)
            return self.browser.find_element(locator)
        except Exception as e:
            raise Exception(f"Element not found: {locator} - {e}")

    def find_elements(self, locator: str, timeout: int = 15) -> List[WebElement]:
        """
        Finds multiple web elements using the given locator. Waits until the page contains the elements.
        Args:
            locator: The locator for the elements.
            timeout: The maximum time to wait for the page to contain the elements (in seconds).
        Returns:
            A list of WebElement objects.
        Raises:
            Exception: If no elements are found within the timeout.
        """
        try:
            self.browser.wait_until_page_contains_element(locator, timeout=timeout)
            return self.browser.find_elements(locator)
        except Exception as e:
            raise Exception(f"Elements not found: {locator} - {e}")

    def enter_text(self, locator: str, text: str, clear_before_enter: bool = True, timeout: int = 15):
        """
        Enters text into a web element.
        Args:
            locator: The locator for the element.
            text: The text to enter.
            clear_before_enter: Whether to clear the field before entering text (default: True).
            timeout: The maximum time to wait for the element to become visible (in seconds).
        Raises:
            Exception: If there is an error entering the text.
        """
        try:
            element = self.find_element(locator, timeout)
            if clear_before_enter:
                element.clear()
            self.browser.input_text(locator, text)
        except Exception as e:
            raise Exception(f"Failed to enter text into {locator}: {e}")

    def enter_text_with_delay(self, locator: str, text: str, delay: float = 0.1, clear_before_enter: bool = True, timeout: int = 15):
        """
        Enters text into a web element with a delay between each character.
      
        Args:
            locator: The locator for the element.
            text: The text to enter.
            delay: The delay between each character (in seconds).
            clear_before_enter: Whether to clear the field before entering text (default: True).
            timeout: The maximum time to wait for the element to become visible (in seconds).
        Raises:
            Exception: If there is an error entering the text.
        """
        try:
            element = self.find_element(locator, timeout)
            if clear_before_enter:
                element.clear()
            for char in text:
                self.browser.input_text(locator, char)
                time.sleep(delay)
        except Exception as e:
            raise Exception(f"Failed to enter text with delay into {locator}: {e}")

    def is_element_visible(self, locator: str, timeout: int = 15) -> bool:
        """
        Checks if a web element is visible.

        Args:
            locator: The locator for the element.
            timeout: The maximum time to wait for the element to be checked (in seconds).
        Returns:
            True if the element is visible, False otherwise.
        Raises:
            Exception: If there is an error checking the visibility.
        """
        try:
            return self.browser.is_element_visible(locator, missing_ok=False)
        except Exception as e:
            raise Exception(f"Error checking visibility of {locator}: {e}")

    def get_text(self, locator: str, timeout: int = 10) -> str:
        """
        Gets the text content of a web element.

        Args:
            locator: The locator for the element.
            timeout: The maximum time to wait for the element to be visible (in seconds).
        Returns:
            The text content of the element.
        Raises:
            Exception: If there is an error getting the text.
        """
        try:
            self.find_element(locator, timeout)
            return self.browser.get_text(locator)
        except Exception as e:
            raise Exception(f"Failed to get text from {locator}: {e}")

    def click_element(self, locator: str, timeout: int = 15):
        """
        Clicks a web element.

        Args:
            locator: The locator for the element.

        Raises:
            Exception: If there is an error clicking the element.
        """
        try:
            self.find_element(locator, timeout)
            self.browser.click_element(locator)
        except Exception as e:
            raise Exception(f"Failed to click element {locator}: {e}")

    def take_screenshot(self, filename: str = "screenshot.png"):
        """
        Takes a screenshot of the current page.

        Args:
            filename: The name of the file to save the screenshot to (default: "screenshot.png").
        Raises:
            Exception: If there is an error taking the screenshot.
        """
        try:
            self.browser.capture_page_screenshot(filename)
        except Exception as e:
            raise Exception(f"Failed to take screenshot: {e}")

    def select_option(self, locator: str, value: str, select_by: str = 'value', timeout: int = 15):
        """
        Selects an option from a dropdown list by its value.

        Args:
            locator: The locator for the dropdown list.
            value: The value of the option to select.
            timeout: The maximum time to wait for the element to become visible (in seconds).
        Raises:
            Exception: If there is an error selecting the option.
        """
        try:
            self.find_element(locator, timeout)
            if select_by == 'value':
                self.browser.select_from_list_by_value(locator, value)
            elif select_by == 'label':
                self.browser.select_from_list_by_label(locator, value)
            else:
                self.browser.select_from_list_by_index(locator, value)
        except Exception as e:
            raise Exception(f"Failed to select option from {locator}: {e}")

    def wait_for_element_to_be_visible(self, locator: str, timeout: int = 15):
        """
        Waits for a specific element to be visible on the page.
        Args:
            locator: The locator of the element to wait for.
            timeout: The maximum time to wait (in seconds).
        Raises:
            Exception: If the element does not become visible within the timeout.
        """
        try:
            self.browser.wait_until_element_is_visible(locator, timeout=timeout)
        except Exception as e:
            raise Exception(f"Element {locator} did not become visible within {timeout} seconds: {e}")

    def is_element_interactable(self, locator: str, timeout: int = 10) -> bool:
            """
            Checks if a web element is interactable (visible and enabled).
            Args:
                locator: The locator for the element.
                timeout: The maximum time to wait for the element to be visible and enabled (in seconds).
            Returns:
                True if the element is interactable, False otherwise.
            """
            try:
                self.find_element(locator, timeout)
                return self.browser.is_element_enabled(locator)
            except Exception:
                return False

    def interact_with_element(self, locator: str, action: str = "click", text: Optional[str] = None, timeout: int = 10):
        """
        Interacts with a web element based on the specified action.

        Args:
            locator: The locator for the element.
            action: The action to perform ("click" or "enter_text"). Defaults to "click".
            text: The text to enter if the action is "enter_text".
            timeout: The maximum time to wait for the element to be interactable (in seconds).
        Raises:
            ValueError: If an invalid action is provided.
            Exception: If the element is not interactable or if there is an error during the interaction.
        """
        try:
            if self.is_element_interactable(locator, timeout):
                if action == "click":
                    self.click_element(locator, timeout)
                elif action == "enter_text":
                    if text is None:
                        raise ValueError("Text must be provided for 'enter_text' action.")
                    self.enter_text(locator, text, timeout=timeout)
                else:
                    raise ValueError(f"Invalid action: {action}")
            else:
                raise Exception(f"Element {locator} is not interactable")
        except Exception as e:
            raise  # Re-raise the caught exception

    def wait_for_load(self, locator: str, timeout: int = 15):
        """
        Waits for a specific element to be present on the page, indicating that the page has loaded.

        Args:
            locator: The locator of the element that signifies page load.
            timeout: The maximum time to wait (in seconds).
        Raises:
            Exception: If the page does not load within the timeout.
        """
        try:
            self.browser.wait_until_page_contains_element(locator, timeout=timeout)
        except Exception as e:
            raise Exception(f"Page did not load within {timeout} seconds: {e}")

    def wait(self, duration: float = 0.5):
        """
        Pauses execution for the specified duration.
        Args:
            duration: The duration to wait in seconds.
        """
        time.sleep(duration)

    def close_browser(self):
        """
        Closes the browser instance.
        Raises:
            Exception: If there is an error closing the browser.
        """
        try:
            self.browser.close_browser()
        except Exception as e:
            raise Exception(f"Failed to close browser: {e}")
