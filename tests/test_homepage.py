"""
Comprehensive UI/UX Automation Tests for PHP Travels Homepage
Using Python, Playwright, and Page Object Model (POM)
"""
from playwright.sync_api import sync_playwright
import pytest
from models.home_page import HomePage

URL_WEB = "https://www.phptravels.net/"


# ==================== NAVIGATION TESTS ====================
class TestNavigationMenu:
    """Test cases for navigation menu"""
    
    def test_logo_visible(self, home_page):
        """TC001: Verify logo is visible on homepage"""
        home_page.verify_logo_visible()
    
    def test_logo_clickable(self, home_page):
        """TC002: Verify logo is clickable"""
        from playwright.sync_api import expect
        expect(home_page.logo).to_be_visible()
        # Logo should be clickable (inside a link)
        expect(home_page.logo.locator("xpath=ancestor::a")).to_be_visible()
    
    def test_navigation_menu_links(self, home_page):
        """TC003: Verify all navigation menu links are visible"""
        home_page.verify_navigation_menu()
    
    def test_navigation_links_clickable(self, home_page):
        """TC004: Verify navigation links are clickable/enabled"""
        from playwright.sync_api import expect
        expect(home_page.flights_nav).to_be_enabled()
        expect(home_page.hotels_nav).to_be_enabled()
        expect(home_page.tours_nav).to_be_enabled()
        expect(home_page.cars_nav).to_be_enabled()
        expect(home_page.visa_nav).to_be_enabled()
        expect(home_page.blogs_nav).to_be_enabled()
    
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


# ==================== SEARCH FORMS TESTS ====================
class TestSearchForms:
    """Test cases for search forms"""
    
    def test_flights_search_form(self, home_page):
        """TC012: Verify flights search form elements"""
        home_page.verify_flights_search_form()
    
    def test_hotels_search_form(self, home_page):
        """TC013: Verify hotels search form elements"""
        home_page.verify_hotels_search_form()
    
    def test_tours_search_form(self, home_page):
        """TC014: Verify tours search form elements"""
        home_page.verify_tours_search_form()
    
    def test_cars_search_form(self, home_page):
        """TC015: Verify cars search form elements"""
        home_page.verify_cars_search_form()
    
    def test_visa_search_form(self, home_page):
        """TC016: Verify visa search form elements"""
        home_page.verify_visa_search_form()
    
    def test_search_forms_inputs_enabled(self, home_page):
        """TC017: Verify search form inputs are enabled/editable"""
        from playwright.sync_api import expect
        # Test flights form inputs
        home_page.click_tab("flights")
        expect(home_page.flying_from_input).to_be_enabled()
        expect(home_page.flying_to_input).to_be_enabled()
        expect(home_page.flight_departure_date).to_be_enabled()
        expect(home_page.flight_search_button).to_be_enabled()


# ==================== FEATURED SECTIONS TESTS ====================
class TestFeaturedSections:
    """Test cases for featured sections"""
    
    def test_featured_flights_section(self, home_page):
        """TC018: Verify featured flights section"""
        home_page.verify_feature_flights_section()
    
    def test_featured_hotels_section(self, home_page):
        """TC019: Verify featured hotels section"""
        home_page.verify_feature_hotels_section()
    
    def test_featured_tours_section(self, home_page):
        """TC020: Verify featured tours section"""
        home_page.verify_feature_tours_section()
    
    def test_featured_cars_section(self, home_page):
        """TC021: Verify featured cars section"""
        home_page.verify_feature_cars_section()


# ==================== FOOTER TESTS ====================
class TestFooterSection:
    """Test cases for footer section"""
    
    def test_footer_visible(self, home_page):
        """TC022: Verify footer section is visible"""
        home_page.verify_footer_section()
    
    def test_footer_links(self, home_page):
        """TC023: Verify footer quick links"""
        home_page.verify_footer_links()
    
    def test_footer_about_contact_links(self, home_page):
        """TC024: Verify footer about and contact links"""
        from playwright.sync_api import expect
        home_page.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        home_page.page.wait_for_timeout(1000)
        expect(home_page.footer_about_link).to_be_attached()
        # Use first() to avoid strict mode violation (multiple contact links)
        expect(home_page.footer_contact_link.first).to_be_attached()
        expect(home_page.footer_copyright).to_be_attached()
    
    def test_newsletter_form(self, home_page):
        """TC025: Verify newsletter signup form"""
        home_page.verify_newsletter_form()
    
    def test_newsletter_form_inputs_enabled(self, home_page):
        """TC026: Verify newsletter form inputs are enabled"""
        from playwright.sync_api import expect
        home_page.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        home_page.page.wait_for_timeout(1000)
        expect(home_page.newsletter_name_input).to_be_enabled()
        expect(home_page.newsletter_email_input).to_be_enabled()
        expect(home_page.newsletter_signup_button).to_be_enabled()


# ==================== COMPLETE HOMEPAGE TEST ====================
class TestCompleteHomepage:
    """Complete homepage test covering all sections"""
    
    def test_complete_homepage_ui(self, home_page):
        """TC027: Complete homepage UI/UX verification"""
        # Verify navigation
        home_page.verify_logo_visible()
        home_page.verify_navigation_menu()
        
        # Verify hero section
        home_page.verify_HomePage_display()
        home_page.verify_search_tabs()
        
        # Verify featured sections
        home_page.verify_feature_flights_section()
        home_page.verify_feature_hotels_section()
        home_page.verify_feature_tours_section()
        home_page.verify_feature_cars_section()
        
        # Verify footer
        home_page.verify_footer_section()
    
    def test_page_title(self, home_page):
        """TC028: Verify page title"""
        import re
        from playwright.sync_api import expect
        expect(home_page.page).to_have_title(re.compile(r"PHP Travels|Travel", re.IGNORECASE))
    
    def test_page_url(self, home_page):
        """TC029: Verify page URL"""
        from playwright.sync_api import expect
        expect(home_page.page).to_have_url("https://www.phptravels.net/")


# ==================== STANDALONE TEST (Original) ====================
def test_homepage():
    """Original standalone test for backward compatibility"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL_WEB, wait_until="domcontentloaded", timeout=90000)
        first_page = HomePage(page)
        first_page.verify_HomePage_display()
        first_page.verify_feature_flights_section()
        first_page.verify_feature_hotels_section()
        first_page.verify_feature_tours_section()
        first_page.verify_feature_cars_section()
        browser.close()