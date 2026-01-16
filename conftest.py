import pytest
from playwright.sync_api import Page, Browser, sync_playwright
from models.home_page import HomePage

@pytest.fixture(scope="function")
def browser():
    """Create a browser instance for each test"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    """Create a new page for each test"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    """Create HomePage object"""
    home = HomePage(page)
    home.navigate()
    home.wait_for_load()
    return home