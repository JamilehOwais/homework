from playwright.sync_api import expect
from pages.inventory_page import InventoryPage

def test_menu_navigation(api_logged_in_page):
    inventory_page = InventoryPage(api_logged_in_page)
    
    inventory_page.open_menu()
    inventory_page.click_about_link()
    
    expect(api_logged_in_page).to_have_url("https://saucelabs.com/")