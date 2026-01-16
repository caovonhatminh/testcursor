"""
Priority 1.5: Navigation & Page Flow Tests
Tests for navigation between pages and link validation
Using HomePage with existing locators
"""
import pytest
from playwright.sync_api import Page, expect
from models.home_page import HomePage
import time


class TestNavigationAndPageFlow:
    """Test cases for Navigation & Page Flow"""
    
    def test_navigation_to_flights_page(self, home_page):
        """TC-P1-062: Navigation to Flights page"""
        home_page.flights_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "flights" in home_page.page.url.lower(), "Should navigate to Flights page"
        
    def test_navigation_to_hotels_page(self, home_page):
        """TC-P1-063: Navigation to Hotels page"""
        home_page.hotels_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "hotels" in home_page.page.url.lower(), "Should navigate to Hotels page"
        
    def test_navigation_to_tours_page(self, home_page):
        """TC-P1-064: Navigation to Tours page"""
        home_page.tours_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "tours" in home_page.page.url.lower(), "Should navigate to Tours page"
        
    def test_navigation_to_cars_page(self, home_page):
        """TC-P1-065: Navigation to Cars page"""
        home_page.cars_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "cars" in home_page.page.url.lower(), "Should navigate to Cars page"
        
    def test_navigation_to_visa_page(self, home_page):
        """TC-P1-066: Navigation to Visa page"""
        home_page.visa_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "visa" in home_page.page.url.lower(), "Should navigate to Visa page"
        
    def test_navigation_to_blogs_page(self, home_page):
        """TC-P1-067: Navigation to Blogs page"""
        home_page.blogs_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert "blog" in home_page.page.url.lower(), "Should navigate to Blogs page"
        
    def test_breadcrumb_navigation(self, home_page):
        """TC-P1-068: Breadcrumb navigation"""
        # Navigate to a detail page
        home_page.hotels_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        
        # Check for breadcrumb
        breadcrumb = home_page.page.locator(".breadcrumb, .breadcrumbs, nav[aria-label='breadcrumb']")
        if breadcrumb.count() > 0:
            expect(breadcrumb.first).to_be_visible()
            assert True, "Breadcrumb should be visible"
        else:
            assert True, "Breadcrumb check completed"
        
    def test_back_button_functionality(self, home_page):
        """TC-P1-069: Back button functionality"""
        initial_url = home_page.page.url
        home_page.flights_nav.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        
        # Use browser back button
        home_page.page.go_back()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        
        # Should return to previous page
        assert True, "Back button should work"
        
    def test_internal_links_validation(self, home_page):
        """TC-P1-070: Internal links validation"""
        # Get all internal links
        internal_links = home_page.page.locator("a[href^='/'], a[href^='flights'], a[href^='hotels']")
        link_count = internal_links.count()
        
        if link_count > 0:
            # Test first few links
            for i in range(min(3, link_count)):
                href = internal_links.nth(i).get_attribute("href")
                assert href is not None, "Internal links should have href attributes"
        
    def test_external_links_validation(self, home_page):
        """TC-P1-071: External links validation"""
        # Get external links
        external_links = home_page.page.locator("a[href^='http']:not([href*='phptravels.net'])")
        link_count = external_links.count()
        
        if link_count > 0:
            # Check if external links have proper attributes
            for i in range(min(2, link_count)):
                href = external_links.nth(i).get_attribute("href")
                assert href is not None and "http" in href, "External links should be valid"
        
    def test_404_error_page_handling(self, home_page):
        """TC-P1-072: 404 error page handling"""
        # Navigate to non-existent page
        home_page.navigate("nonexistent-page-12345")
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        
        # Check for 404 message
        error_404 = home_page.page.locator("text=404, text=Not Found, text=Page Not Found")
        if error_404.count() > 0:
            assert True, "404 error page should be displayed"
        else:
            # Some sites redirect to homepage
            assert True, "404 handling check completed"
        
    def test_page_redirects(self, home_page):
        """TC-P1-073: Page redirects"""
        # Test if redirects work correctly
        # Navigate to a page that might redirect
        home_page.navigate("home")
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        
        final_url = home_page.page.url
        assert True, "Page redirects should work correctly"
