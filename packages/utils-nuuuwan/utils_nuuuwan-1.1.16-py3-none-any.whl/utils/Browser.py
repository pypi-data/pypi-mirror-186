"""Browser utils."""


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import browser_firefox_profile
from utils.Log import Log

MAX_T_WAIT = 60


class Browser:
    """Browser."""

    def __init__(self):
        """Construct."""
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(
            options=options,
            firefox_profile=browser_firefox_profile.get_firefox_profile(),
        )
        self.log = Log('Browser')
        self.log.debug('Opened Selenium Firefox Browser.')

    def open(self, url: str):
        self.browser.get(url)
        self.log.debug(f'Opened "{url}".')

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        SCRIPT_SCROLL = 'window.scrollTo(0, document.body.scrollHeight);'
        self.browser.execute_script(SCRIPT_SCROLL)

    @property
    def source(self):
        """Get page source."""
        return self.browser.page_source

    def quit(self):
        """Quit."""
        self.browser.close()
        self.browser.quit()
