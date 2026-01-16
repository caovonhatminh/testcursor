from playwright.sync_api import sync_playwright
import pytest
from models.home_page import HomePage

URL_WEB = "https://www.phptravels.net/"


# ==================== NAVIGATION TESTS ====================
class TestNavigationMenu:
    """Test cases for navigation menu"""
    
    # def test_logo_visible(self, home_page):
    #     """TC001: Verify logo is visible on homepage"""
    #     home_page.verify_logo_visible()
    
    # def test_logo_clickable(self, home_page):
    #     """TC002: Verify logo is clickable"""
    #     from playwright.sync_api import expect
    #     expect(home_page.logo).to_be_visible()
    #     # Logo should be clickable (inside a link)
    #     expect(home_page.logo.locator("xpath=ancestor::a")).to_be_visible()
    
    # def test_navigation_menu_links(self, home_page):
    #     """TC003: Verify all navigation menu links are visible"""
    #     home_page.verify_navigation_menu()
    
    # def test_navigation_links_clickable(self, home_page):
    #     """TC004: Verify navigation links are clickable/enabled"""
    #     from playwright.sync_api import expect
    #     expect(home_page.flights_nav).to_be_enabled()
    #     expect(home_page.hotels_nav).to_be_enabled()
    #     expect(home_page.tours_nav).to_be_enabled()
    #     expect(home_page.cars_nav).to_be_enabled()
    #     expect(home_page.visa_nav).to_be_enabled()
    #     expect(home_page.blogs_nav).to_be_enabled()
    
    def test_dropdown_menus(self, home_page):
        """TC005: Verify dropdown menus are visible"""
        home_page.verify_dropdown_menus()
    
    def test_dropdown_menus_clickable(self, home_page):
        """TC006: Verify dropdown menus are clickable/enabled"""
        from playwright.sync_api import expect
        expect(home_page.language_dropdown).to_be_enabled()
        expect(home_page.currency_dropdown).to_be_enabled()
        expect(home_page.agents_dropdown).to_be_enabled()
        expect(home_page.customer_dropdown).to_be_enabled()


# ==================== HERO SECTION TESTS ====================
class TestHeroSection:
    """Test cases for hero section"""
    
    def test_hero_banner_display(self, home_page):
        """TC007: Verify hero banner is displayed"""
        home_page.verify_HomePage_display()
    
    def test_hero_title_and_tagline(self, home_page):
        """TC008: Verify hero title and tagline"""
        home_page.verify_hero_section()
    
    def test_search_tabs_visible(self, home_page):
        """TC009: Verify all 5 search tabs are visible"""
        home_page.verify_search_tabs()
    
    def test_search_tabs_clickable(self, home_page):
        """TC010: Verify search tabs are clickable/enabled"""
        from playwright.sync_api import expect
        expect(home_page.flights_tab).to_be_enabled()
        expect(home_page.hotels_tab).to_be_enabled()
        expect(home_page.tours_tab).to_be_enabled()
        expect(home_page.cars_tab).to_be_enabled()
        expect(home_page.visa_tab).to_be_enabled()
    
    def test_tab_switching(self, home_page):
        """TC011: Verify tabs can be switched"""
        home_page.click_tab("flights")
        home_page.click_tab("hotels")
        home_page.click_tab("tours")
        home_page.click_tab("cars")
        home_page.click_tab("visa")
