from playwright.sync_api import Page, expect
import time

class BasePage:
    """Base class for all page objects with common utilities"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.phptravels.net/"
    
    def navigate(self, path: str = ""):
        """Navigate to base URL or specific path"""
        self.page.goto(self.base_url + path, wait_until="domcontentloaded", timeout=90000)
    
    def wait_for_load(self):
        """Wait for page load state"""
        self.page.wait_for_load_state("domcontentloaded")
    
    def scroll_to_element(self, locator):
        """Scroll element into view"""
        locator.scroll_into_view_if_needed()
        time.sleep(0.5)
    
    def is_element_visible(self, locator, timeout: int = 5000) -> bool:
        """Check if element is visible within timeout"""
        try:
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False
    
    def wait_and_click(self, locator, timeout: int = 10000):
        """Wait for element and click"""
        locator.wait_for(state="visible", timeout=timeout)
        locator.click()
    
    def take_screenshot(self, name: str):
        """Take screenshot with given name"""
        self.page.screenshot(path=f"screenshots/{name}.png")