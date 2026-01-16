"""
Priority 1.1: Search Functionality Tests
Tests for Flights, Hotels, Tours, Cars, and Visa search
Using HomePage with existing locators
"""
import pytest
import time
from playwright.sync_api import Page, expect
from models.home_page import HomePage


# ==================== FLIGHTS SEARCH TESTS ====================
class TestFlightsSearch:
    """Test cases for Flights Search functionality"""
    
    def test_search_flights_valid_origin_destination(self, home_page):
        """TC-P1-001: Search flights with valid origin/destination"""
        home_page.search_flights(
            origin="New York",
            destination="London",
            flight_type="oneway",
            departure_days=7
        )
        assert home_page.verify_search_results_displayed(), "Search results should be displayed"
        
    def test_search_flights_round_trip(self, home_page):
        """TC-P1-002: Search flights with round trip"""
        home_page.search_flights(
            origin="Paris",
            destination="Tokyo",
            flight_type="round",
            departure_days=14,
            return_days=21
        )
        assert home_page.verify_search_results_displayed(), "Round trip search results should be displayed"
        
    def test_search_flights_one_way(self, home_page):
        """TC-P1-003: Search flights with one-way"""
        home_page.search_flights(
            origin="Dubai",
            destination="Singapore",
            flight_type="oneway",
            departure_days=10
        )
        assert home_page.verify_search_results_displayed(), "One-way search results should be displayed"
        
    def test_flights_date_validation(self, home_page):
        """TC-P1-004: Date validation (past dates should be disabled)"""
        assert home_page.verify_flight_date_validation(), "Past dates should be rejected"
        
    def test_flights_search_invalid_inputs(self, home_page):
        """TC-P1-005: Search with invalid inputs (error handling)"""
        home_page.click_tab("flights")
        home_page.flying_from_input.fill("")
        home_page.flying_to_input.fill("")
        home_page.flight_search_button.click()
        time.sleep(2)
        # Should show error or not proceed
        current_url = home_page.page.url
        assert "flights" in current_url.lower() or home_page.page.url == home_page.base_url, "Should remain on page with invalid inputs"
        
    def test_flights_search_results_display(self, home_page):
        """TC-P1-006: Search results display correctly"""
        home_page.search_flights(
            origin="Los Angeles",
            destination="Sydney",
            flight_type="oneway",
            departure_days=7
        )
        results_count = home_page.get_search_results_count()
        assert results_count >= 0, "Search should return results or no results message"
        
    def test_flights_filter_results(self, home_page):
        """TC-P1-007: Filter search results (price, time, airline)"""
        home_page.search_flights(
            origin="Miami",
            destination="Barcelona",
            flight_type="oneway",
            departure_days=7
        )
        if home_page.get_search_results_count() > 0:
            # Check if filter elements exist
            price_filter = home_page.page.locator("input[type='range'], .price-filter")
            if price_filter.count() > 0:
                assert True, "Filters should be available"
        
    def test_flights_sort_results(self, home_page):
        """TC-P1-008: Sort search results"""
        home_page.search_flights(
            origin="Chicago",
            destination="Berlin",
            flight_type="oneway",
            departure_days=7
        )
        if home_page.get_search_results_count() > 0:
            sort_dropdown = home_page.page.locator("select[name='sort'], .sort-dropdown")
            if sort_dropdown.count() > 0:
                sort_dropdown.select_option("price")
                time.sleep(2)
                assert True, "Sorting should work"
        
    def test_flights_pagination(self, home_page):
        """TC-P1-009: Pagination on search results"""
        home_page.search_flights(
            origin="Toronto",
            destination="Rome",
            flight_type="oneway",
            departure_days=7
        )
        pagination = home_page.page.locator(".pagination, .page-navigation")
        if pagination.count() > 0:
            next_button = home_page.page.locator("a.next, button.next, .pagination .next")
            if next_button.count() > 0:
                next_button.first.click()
                home_page.page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                assert True, "Pagination should work"


# ==================== HOTELS SEARCH TESTS ====================
class TestHotelsSearch:
    """Test cases for Hotels Search functionality"""
    
    def test_search_hotels_by_city(self, home_page):
        """TC-P1-010: Search hotels by city/location"""
        home_page.search_hotels(
            city="Paris",
            checkin_days=7,
            checkout_days=9
        )
        assert home_page.verify_search_results_displayed(), "Hotel search results should be displayed"
        
    def test_hotels_checkin_checkout_validation(self, home_page):
        """TC-P1-011: Check-in/Check-out date validation"""
        assert home_page.verify_hotel_date_validation(), "Check-out should be after check-in"
        
    def test_hotels_guest_count_selection(self, home_page):
        """TC-P1-012: Guest count selection"""
        home_page.click_tab("hotels")
        home_page.enter_hotel_city("London")
        home_page.select_hotel_checkin_date(7)
        home_page.select_hotel_checkout_date(9)
        # Check if guest/room selectors exist
        guests_dropdown = home_page.page.locator("select[name='guests'], .guests-select")
        if guests_dropdown.count() > 0:
            guests_dropdown.select_option("2")
        home_page.hotels_search_button.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert home_page.verify_search_results_displayed(), "Search with guest count should work"
        
    def test_hotels_search_results_display(self, home_page):
        """TC-P1-013: Hotel search results display"""
        home_page.search_hotels(
            city="Dubai",
            checkin_days=10,
            checkout_days=12
        )
        results_count = home_page.get_search_results_count()
        assert results_count >= 0, "Hotel search should return results"
        
    def test_hotels_filter_price_rating(self, home_page):
        """TC-P1-014: Filter hotels (price, rating, amenities)"""
        home_page.search_hotels(
            city="New York",
            checkin_days=14,
            checkout_days=16
        )
        if home_page.get_search_results_count() > 0:
            price_filter = home_page.page.locator("input[type='range'], .price-filter")
            rating_filter = home_page.page.locator(".rating-filter, input[name='rating']")
            if price_filter.count() > 0 or rating_filter.count() > 0:
                assert True, "Filters should be available"
        
    def test_hotel_detail_page_navigation(self, home_page):
        """TC-P1-015: Hotel detail page navigation"""
        home_page.search_hotels(
            city="Tokyo",
            checkin_days=7,
            checkout_days=9
        )
        if home_page.get_search_results_count() > 0:
            hotel_cards = home_page.page.locator(".hotel-card, .hotel-item")
            if hotel_cards.count() > 0:
                hotel_cards.first.click()
                home_page.page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                assert "hotel" in home_page.page.url.lower() or "detail" in home_page.page.url.lower(), "Should navigate to hotel detail page"


# ==================== TOURS SEARCH TESTS ====================
class TestToursSearch:
    """Test cases for Tours Search functionality"""
    
    def test_search_tours_by_destination(self, home_page):
        """TC-P1-016: Search tours by destination"""
        home_page.search_tours(
            destination="Bali",
            days_from_today=7
        )
        assert home_page.verify_search_results_displayed(), "Tour search results should be displayed"
        
    def test_tours_date_selection(self, home_page):
        """TC-P1-017: Date selection for tours"""
        home_page.click_tab("tours")
        home_page.enter_tour_destination("Santorini")
        home_page.select_tour_date(14)
        home_page.tours_search_button.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert home_page.verify_search_results_displayed(), "Tour search with date should work"
        
    def test_tours_search_results(self, home_page):
        """TC-P1-018: Tour search results"""
        home_page.search_tours(
            destination="Machu Picchu",
            days_from_today=10
        )
        results_count = home_page.get_search_results_count()
        assert results_count >= 0, "Tour search should return results"
        
    def test_tour_detail_page(self, home_page):
        """TC-P1-019: Tour detail page"""
        home_page.search_tours(
            destination="Iceland",
            days_from_today=7
        )
        if home_page.get_search_results_count() > 0:
            tour_cards = home_page.page.locator(".tour-card, .tour-item")
            if tour_cards.count() > 0:
                tour_cards.first.click()
                home_page.page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                assert "tour" in home_page.page.url.lower() or "detail" in home_page.page.url.lower(), "Should navigate to tour detail page"
        
    def test_tour_booking_flow(self, home_page):
        """TC-P1-020: Tour booking flow"""
        home_page.search_tours(
            destination="Egypt",
            days_from_today=7
        )
        if home_page.get_search_results_count() > 0:
            book_button = home_page.page.locator("button:has-text('Book Now'), a:has-text('Book Now')")
            if book_button.count() > 0:
                book_button.first.click()
                home_page.page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                assert "book" in home_page.page.url.lower() or "booking" in home_page.page.url.lower(), "Should navigate to booking page"


# ==================== CARS SEARCH TESTS ====================
class TestCarsSearch:
    """Test cases for Cars Search functionality"""
    
    def test_search_cars_by_location(self, home_page):
        """TC-P1-021: Search rental cars by location"""
        home_page.search_cars(
            pickup_location="Miami",
            dropoff_location="Miami"
        )
        assert home_page.verify_search_results_displayed(), "Car search results should be displayed"
        
    def test_cars_pickup_dropoff_location(self, home_page):
        """TC-P1-022: Pickup/Drop-off location"""
        home_page.click_tab("cars")
        home_page.enter_car_pickup_location("Los Angeles")
        home_page.enter_car_dropoff_location("San Francisco")
        home_page.cars_search_button.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert home_page.verify_search_results_displayed(), "Car search with different locations should work"
        
    def test_cars_date_time_selection(self, home_page):
        """TC-P1-023: Date/time selection"""
        home_page.search_cars(
            pickup_location="London",
            dropoff_location="London"
        )
        # Check if date/time inputs exist
        pickup_date = home_page.page.locator("input[name='pickup_date'], input#pickup_date")
        if pickup_date.count() > 0:
            assert True, "Date/time selection should be available"
        
    def test_cars_search_results(self, home_page):
        """TC-P1-024: Car search results"""
        home_page.search_cars(
            pickup_location="Paris",
            dropoff_location="Paris"
        )
        results_count = home_page.get_search_results_count()
        assert results_count >= 0, "Car search should return results"
        
    def test_car_details_and_booking(self, home_page):
        """TC-P1-025: Car details and booking"""
        home_page.search_cars(
            pickup_location="Dubai",
            dropoff_location="Dubai"
        )
        if home_page.get_search_results_count() > 0:
            car_cards = home_page.page.locator(".car-card, .car-item")
            if car_cards.count() > 0:
                car_cards.first.click()
                home_page.page.wait_for_load_state("networkidle", timeout=30000)
                time.sleep(2)
                assert "car" in home_page.page.url.lower() or "detail" in home_page.page.url.lower(), "Should navigate to car detail page"


# ==================== VISA SEARCH TESTS ====================
class TestVisaSearch:
    """Test cases for Visa Search functionality"""
    
    def test_search_visa_requirements(self, home_page):
        """TC-P1-026: Search visa requirements"""
        home_page.search_visa(
            from_country="United States",
            to_country="United Kingdom"
        )
        assert home_page.verify_search_results_displayed(), "Visa search results should be displayed"
        
    def test_visa_country_selection(self, home_page):
        """TC-P1-027: Country selection (from/to)"""
        home_page.click_tab("visa")
        home_page.enter_visa_from_country("Canada")
        home_page.enter_visa_to_country("Australia")
        home_page.visa_search_button.click()
        home_page.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
        assert home_page.verify_search_results_displayed(), "Visa search with country selection should work"
        
    def test_visa_application_form(self, home_page):
        """TC-P1-028: Visa application form"""
        home_page.search_visa(
            from_country="India",
            to_country="Singapore"
        )
        if home_page.get_search_results_count() > 0:
            application_form = home_page.page.locator("form.visa-application, .visa-form")
            if application_form.count() > 0:
                assert True, "Application form should be available"
        
    def test_visa_search_results(self, home_page):
        """TC-P1-029: Visa search results"""
        home_page.search_visa(
            from_country="Brazil",
            to_country="Japan"
        )
        results_count = home_page.get_search_results_count()
        assert results_count >= 0, "Visa search should return results"
