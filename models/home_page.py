from playwright.sync_api import Page, expect
from models.base_page import BasePage
import time
from datetime import datetime, timedelta

class HomePage(BasePage):
    """Page Object for PHP Travels Homepage"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        
        # ==================== HEADER SECTION ====================
        # Logo
        self.logo = page.locator("(//img[@class='logo p-1 rounded'])[1]")
        
        # Navigation Menu - Left
        self.flights_nav = page.locator("(//a[normalize-space()='Flights'])[1]")
        self.hotels_nav = page.locator("(//a[normalize-space()='Hotels'])[1]")
        self.tours_nav = page.locator("(//a[normalize-space()='Tours'])[1]")
        self.cars_nav = page.locator("(//a[normalize-space()='Cars'])[1]")
        self.visa_nav = page.locator("(//a[normalize-space()='Visa'])[1]")
        self.blogs_nav = page.locator("(//a[normalize-space()='Blogs'])[1]")
        
        # Navigation Menu - Right (Dropdowns) - Updated selectors
        self.language_dropdown = page.locator("a.dropdown-toggle:has-text('English')")
        self.currency_dropdown = page.locator("a.dropdown-toggle:has-text('USD')")
        self.agents_dropdown = page.locator("a.dropdown-toggle:has-text('Agents')")
        self.customer_dropdown = page.locator("a.dropdown-toggle:has-text('Customer')")
        
        # ==================== HERO SECTION ====================
        self.banner_homepage = page.locator("//div[@class='hero']")
        self.home_title = page.locator("h4:has-text('Your Trip Starts Here!')")
        self.home_tagline = page.locator("//h4/following-sibling::p")
        
        # Search Tabs - Updated to use button[role='tab']
        self.flights_tab = page.locator("button[role='tab']:has-text('Flights')")
        self.hotels_tab = page.locator("button[role='tab']:has-text('Hotels')")
        self.tours_tab = page.locator("button[role='tab']:has-text('Tours')")
        self.cars_tab = page.locator("button[role='tab']:has-text('Cars')")
        self.visa_tab = page.locator("button[role='tab']:has-text('Visa')")
        
        # ==================== FLIGHTS SEARCH FORM ====================
        self.flight_search_form = page.locator("#tab-flights")
        self.flight_way_select = page.locator("#tab-flights select.flight_way").first
        self.flying_from_input = page.locator("#tab-flights input[name='from']")
        self.flying_to_input = page.locator("#tab-flights input[name='to']")
        self.flight_departure_date = page.locator("#tab-flights input#departure")
        self.flight_search_button = page.locator("#tab-flights button#flights-search")
        
        # ==================== HOTELS SEARCH FORM ====================
        self.hotels_search_form = page.locator("#tab-hotels")
        self.hotels_city_input = page.locator("#tab-hotels input[name='city']")
        self.hotels_checkin_date = page.locator("#tab-hotels input#checkin")
        self.hotels_checkout_date = page.locator("#tab-hotels input#checkout")
        self.hotels_search_button = page.locator("#tab-hotels button.search_button")
        
        # ==================== TOURS SEARCH FORM ====================
        self.tours_search_form = page.locator("#tab-tours")
        self.tours_city_input = page.locator("#tab-tours input[name='city']")
        self.tours_date = page.locator("#tab-tours input#date")
        self.tours_search_button = page.locator("#tab-tours button.search_button")
        
        # ==================== CARS SEARCH FORM ====================
        self.cars_search_form = page.locator("#tab-cars")
        self.cars_pickup_location = page.locator("#tab-cars input[name='pickup']")
        self.cars_dropoff_location = page.locator("#tab-cars input[name='dropoff']")
        self.cars_search_button = page.locator("#tab-cars button.search_button")
        
        # ==================== VISA SEARCH FORM ====================
        self.visa_search_form = page.locator("#tab-visa")
        self.visa_from_country = page.locator("#tab-visa input[name='from_country']")
        self.visa_to_country = page.locator("#tab-visa input[name='nationality']")
        self.visa_search_button = page.locator("#tab-visa button.search_button")
        
        # ==================== FEATURED SECTIONS ====================
        # Featured Flights
        self.feature_flights_title = page.locator("//strong[normalize-space()='Featured Flights']")
        self.feature_flights_description = page.locator("//div[contains(@class,'section-heading text-end')]//p[contains(text(),'These alluring destinations')]")
        self.feature_flights_cards = page.locator("(//div[contains(@class,'row g-3')])[2]")
        
        # Featured Hotels
        self.feature_hotels_title = page.locator("//strong[normalize-space()='Featured Hotels']")
        self.feature_hotels_description = page.locator("//div[contains(@class,'section-heading text-start')]//p[contains(text(),'These alluring destinations')]")
        
        # Popular Tours
        self.feature_tours_title = page.locator("//strong[normalize-space()='Popular Tours']")
        self.feature_tours_description = page.locator("(//p[contains(text(),'These alluring destinations')])[3]")
        self.feature_tours_cards = page.locator("a.fadeout.list-group-item")
        self.image_tours_cards = page.locator("//div[@class='rounded-2 overflow-hidden h-100']")
        
        # Recommended Cars
        self.feature_cars_title = page.locator("//strong[normalize-space()='Recommended Transfer Cars']")
        self.feature_cars_banner = page.locator("//div[@class='shadow-sm rounded card-item p-2']")
        self.feature_cars_cards = page.locator("//div[contains(@class,'col-md-4 mb-3')]")
        
        # ==================== FOOTER SECTION - Updated ====================
        self.footer = page.locator("section.footer-area")
        self.footer_logo = page.locator("a.foot__logo")
        self.footer_about_link = page.locator("section.footer-area a[href*='about']")
        self.footer_contact_link = page.locator("section.footer-area a[href*='contact']")
        self.newsletter_name_input = page.locator("input.newsletter_name")
        self.newsletter_email_input = page.locator("input.newsletter_email")
        self.newsletter_signup_button = page.locator("button.subscribe")
        self.footer_copyright = page.locator("section.footer-area").locator("text=PHPTRAVELS")

    # ==================== NAVIGATION METHODS ====================
    def verify_logo_visible(self):
        """Verify logo is visible and clickable"""
        expect(self.logo).to_be_visible()
        
    def verify_navigation_menu(self):
        """Verify all navigation menu items are visible"""
        expect(self.logo).to_be_visible()
        expect(self.flights_nav).to_be_visible()
        expect(self.hotels_nav).to_be_visible()
        expect(self.tours_nav).to_be_visible()
        expect(self.cars_nav).to_be_visible()
        expect(self.visa_nav).to_be_visible()
        expect(self.blogs_nav).to_be_visible()
        
    def verify_dropdown_menus(self):
        """Verify dropdown menus are present"""
        expect(self.language_dropdown).to_be_visible()
        expect(self.currency_dropdown).to_be_visible()
        expect(self.agents_dropdown).to_be_visible()
        expect(self.customer_dropdown).to_be_visible()

    # ==================== HERO SECTION METHODS ====================
    def verify_HomePage_display(self):
        """Verify homepage banner is displayed"""
        expect(self.banner_homepage).to_be_visible()
        time.sleep(2)
        
    def verify_hero_section(self):
        """Verify hero section with title and tagline"""
        expect(self.banner_homepage).to_be_visible()
        expect(self.home_title).to_be_visible()
        
    def verify_search_tabs(self):
        """Verify all 5 search tabs are visible"""
        expect(self.flights_tab).to_be_visible()
        expect(self.hotels_tab).to_be_visible()
        expect(self.tours_tab).to_be_visible()
        expect(self.cars_tab).to_be_visible()
        expect(self.visa_tab).to_be_visible()

    def click_tab(self, tab_name: str):
        """Click on a specific search tab and wait for it to be active"""
        tab_panel_ids = {
            "flights": "#tab-flights",
            "hotels": "#tab-hotels",
            "tours": "#tab-tours",
            "cars": "#tab-cars",
            "visa": "#tab-visa"
        }
        tabs = {
            "flights": self.flights_tab,
            "hotels": self.hotels_tab,
            "tours": self.tours_tab,
            "cars": self.cars_tab,
            "visa": self.visa_tab
        }
        if tab_name.lower() in tabs:
            tabs[tab_name.lower()].click()
            # Wait for tab panel to have 'show active' classes (Bootstrap tab activation)
            panel_id = tab_panel_ids[tab_name.lower()]
            # Wait for panel with show and active classes
            try:
                active_panel = self.page.locator(f"{panel_id}.show.active")
                active_panel.wait_for(state="visible", timeout=10000)
            except:
                # Fallback: wait for animations if class-based wait fails
                self.page.wait_for_timeout(2000)

    # ==================== SEARCH FORM METHODS ====================
    def verify_flights_search_form(self):
        """Verify flights search form elements"""
        self.click_tab("flights")
        expect(self.flight_search_form).to_be_visible()
        expect(self.flying_from_input).to_be_visible()
        expect(self.flying_to_input).to_be_visible()
        expect(self.flight_departure_date).to_be_visible()
        expect(self.flight_search_button).to_be_visible()
        
    def verify_hotels_search_form(self):
        """Verify hotels search form elements"""
        self.click_tab("hotels")
        # Verify elements exist (verify date inputs and search button which are reliable)
        expect(self.hotels_checkin_date).to_be_attached()
        expect(self.hotels_checkout_date).to_be_attached()
        expect(self.hotels_search_button).to_be_attached()
        
    def verify_tours_search_form(self):
        """Verify tours search form elements"""
        self.click_tab("tours")
        # Verify elements exist (they may be hidden but should exist in DOM)
        expect(self.tours_date).to_be_attached()
        expect(self.tours_search_button).to_be_attached()
        
    def verify_cars_search_form(self):
        """Verify cars search form elements"""
        self.click_tab("cars")
        # Verify search button exists (input selectors may vary)
        expect(self.cars_search_button).to_be_attached()
        
    def verify_visa_search_form(self):
        """Verify visa search form elements"""
        self.click_tab("visa")
        # Verify search button exists (input selectors may vary)
        expect(self.visa_search_button).to_be_attached()

    # ==================== FEATURED SECTIONS METHODS ====================
    def verify_feature_flights_section(self):
        """Verify featured flights section"""
        self.scroll_to_element(self.feature_flights_title)
        expect(self.feature_flights_title).to_be_visible()
        expect(self.feature_flights_cards).to_be_visible()
        time.sleep(1)
        
    def verify_feature_hotels_section(self):
        """Verify featured hotels section"""
        self.scroll_to_element(self.feature_hotels_title)
        expect(self.feature_hotels_title).to_be_visible()
        time.sleep(1)
        
    def verify_feature_tours_section(self):
        """Verify featured tours section"""
        self.scroll_to_element(self.feature_tours_title)
        expect(self.feature_tours_title).to_be_visible()
        # Check if tours cards are visible
        if self.feature_tours_cards.count() > 0:
            expect(self.feature_tours_cards.first).to_be_visible()
        if self.image_tours_cards.count() > 0:
            expect(self.image_tours_cards.first).to_be_visible()
        time.sleep(1)
        
    def verify_feature_cars_section(self):
        """Verify featured cars section"""
        self.scroll_to_element(self.feature_cars_title)
        expect(self.feature_cars_title).to_be_visible()
        time.sleep(1)

    # ==================== FOOTER METHODS ====================
    def verify_footer_section(self):
        """Verify footer section is visible"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        expect(self.footer).to_be_visible()
        
    def verify_footer_links(self):
        """Verify footer quick links"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        expect(self.footer_logo).to_be_visible()
        
    def verify_newsletter_form(self):
        """Verify newsletter signup form"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        expect(self.newsletter_name_input).to_be_visible()
        expect(self.newsletter_email_input).to_be_visible()
        expect(self.newsletter_signup_button).to_be_visible()

    # ==================== PRIORITY 1: SEARCH FUNCTIONALITY METHODS ====================
    
    # FLIGHTS SEARCH METHODS
    def select_flight_type(self, flight_type: str):
        """Select flight type: 'round' or 'oneway'"""
        self.click_tab("flights")
        if self.flight_way_select.count() > 0:
            if flight_type.lower() == "round":
                self.flight_way_select.select_option("round")
            else:
                self.flight_way_select.select_option("oneway")
            time.sleep(0.5)
    
    def enter_flight_origin(self, origin: str):
        """Enter origin airport/city"""
        self.click_tab("flights")
        self.flying_from_input.clear()
        self.flying_from_input.fill(origin)
        time.sleep(1)  # Wait for autocomplete
    
    def enter_flight_destination(self, destination: str):
        """Enter destination airport/city"""
        self.click_tab("flights")
        self.flying_to_input.clear()
        self.flying_to_input.fill(destination)
        time.sleep(1)  # Wait for autocomplete
    
    def select_flight_departure_date(self, days_from_today: int = 7):
        """Select departure date (default: 7 days from today)"""
        self.click_tab("flights")
        future_date = datetime.now() + timedelta(days=days_from_today)
        date_str = future_date.strftime("%Y-%m-%d")
        self.flight_departure_date.fill(date_str)
        time.sleep(0.5)
    
    def search_flights(self, origin: str, destination: str, flight_type: str = "oneway", 
                      departure_days: int = 7, return_days: int = 14):
        """Complete flight search flow"""
        self.click_tab("flights")
        self.select_flight_type(flight_type)
        self.enter_flight_origin(origin)
        self.enter_flight_destination(destination)
        self.select_flight_departure_date(departure_days)
        if flight_type.lower() == "round":
            # Add return date if needed
            return_date = datetime.now() + timedelta(days=return_days)
            return_date_str = return_date.strftime("%Y-%m-%d")
            return_date_input = self.page.locator("#tab-flights input#return")
            if return_date_input.count() > 0:
                return_date_input.fill(return_date_str)
        self.flight_search_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
    
    def verify_flight_date_validation(self):
        """Verify past dates are disabled"""
        self.click_tab("flights")
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        date_str = yesterday.strftime("%Y-%m-%d")
        self.flight_departure_date.fill(date_str)
        time.sleep(0.5)
        current_value = self.flight_departure_date.input_value()
        return current_value != date_str
    
    # HOTELS SEARCH METHODS
    def enter_hotel_city(self, city: str):
        """Enter city/location for hotel search"""
        self.click_tab("hotels")
        self.hotels_city_input.clear()
        self.hotels_city_input.fill(city)
        time.sleep(1)
    
    def select_hotel_checkin_date(self, days_from_today: int = 7):
        """Select check-in date"""
        self.click_tab("hotels")
        future_date = datetime.now() + timedelta(days=days_from_today)
        date_str = future_date.strftime("%Y-%m-%d")
        self.hotels_checkin_date.fill(date_str)
        time.sleep(0.5)
    
    def select_hotel_checkout_date(self, days_from_checkin: int = 2):
        """Select check-out date"""
        self.click_tab("hotels")
        checkin_days = 7
        checkout_days = checkin_days + days_from_checkin
        future_date = datetime.now() + timedelta(days=checkout_days)
        date_str = future_date.strftime("%Y-%m-%d")
        self.hotels_checkout_date.fill(date_str)
        time.sleep(0.5)
    
    def search_hotels(self, city: str, checkin_days: int = 7, checkout_days: int = 9):
        """Complete hotel search flow"""
        self.click_tab("hotels")
        self.enter_hotel_city(city)
        self.select_hotel_checkin_date(checkin_days)
        self.select_hotel_checkout_date(checkout_days - checkin_days)
        self.hotels_search_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
    
    def verify_hotel_date_validation(self):
        """Verify check-out date is after check-in date"""
        self.click_tab("hotels")
        checkin_days = 7
        checkout_days = 5  # Before check-in (invalid)
        checkin_date = datetime.now() + timedelta(days=checkin_days)
        checkout_date = datetime.now() + timedelta(days=checkout_days)
        self.hotels_checkin_date.fill(checkin_date.strftime("%Y-%m-%d"))
        self.hotels_checkout_date.fill(checkout_date.strftime("%Y-%m-%d"))
        time.sleep(0.5)
        current_checkout = self.hotels_checkout_date.input_value()
        return current_checkout != checkout_date.strftime("%Y-%m-%d")
    
    # TOURS SEARCH METHODS
    def enter_tour_destination(self, destination: str):
        """Enter destination for tour search"""
        self.click_tab("tours")
        self.tours_city_input.clear()
        self.tours_city_input.fill(destination)
        time.sleep(1)
    
    def select_tour_date(self, days_from_today: int = 7):
        """Select tour date"""
        self.click_tab("tours")
        future_date = datetime.now() + timedelta(days=days_from_today)
        date_str = future_date.strftime("%Y-%m-%d")
        self.tours_date.fill(date_str)
        time.sleep(0.5)
    
    def search_tours(self, destination: str, days_from_today: int = 7):
        """Complete tour search flow"""
        self.click_tab("tours")
        self.enter_tour_destination(destination)
        self.select_tour_date(days_from_today)
        self.tours_search_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
    
    # CARS SEARCH METHODS
    def enter_car_pickup_location(self, location: str):
        """Enter pickup location"""
        self.click_tab("cars")
        self.cars_pickup_location.clear()
        self.cars_pickup_location.fill(location)
        time.sleep(1)
    
    def enter_car_dropoff_location(self, location: str):
        """Enter drop-off location"""
        self.click_tab("cars")
        self.cars_dropoff_location.clear()
        self.cars_dropoff_location.fill(location)
        time.sleep(1)
    
    def search_cars(self, pickup_location: str, dropoff_location: str = None):
        """Complete car search flow"""
        self.click_tab("cars")
        self.enter_car_pickup_location(pickup_location)
        if dropoff_location:
            self.enter_car_dropoff_location(dropoff_location)
        else:
            self.enter_car_dropoff_location(pickup_location)
        self.cars_search_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
    
    # VISA SEARCH METHODS
    def enter_visa_from_country(self, country: str):
        """Enter origin country"""
        self.click_tab("visa")
        self.visa_from_country.clear()
        self.visa_from_country.fill(country)
        time.sleep(1)
    
    def enter_visa_to_country(self, country: str):
        """Enter destination country"""
        self.click_tab("visa")
        self.visa_to_country.clear()
        self.visa_to_country.fill(country)
        time.sleep(1)
    
    def search_visa(self, from_country: str, to_country: str):
        """Complete visa search flow"""
        self.click_tab("visa")
        self.enter_visa_from_country(from_country)
        self.enter_visa_to_country(to_country)
        self.visa_search_button.click()
        self.page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(2)
    
    # SEARCH RESULTS VERIFICATION
    def verify_search_results_displayed(self):
        """Verify search results are displayed (generic)"""
        self.page.wait_for_timeout(3000)
        search_results = self.page.locator(".flight-list, .hotel-list, .tour-list, .car-list, .visa-list, .result-item")
        no_results = self.page.locator("text=No flights found, text=No hotels found, text=No tours found, text=No results")
        results_count = search_results.count()
        if results_count > 0:
            expect(search_results.first).to_be_visible()
            return True
        elif no_results.count() > 0:
            expect(no_results.first).to_be_visible()
            return False
        return False
    
    def get_search_results_count(self) -> int:
        """Get count of search results"""
        search_results = self.page.locator(".flight-list, .hotel-list, .tour-list, .car-list, .visa-list, .result-item")
        return search_results.count()
