from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.about_sidebar_link = page.locator("#about_sidebar_link")

    def open_menu(self):
        self.menu_button.click()
        expect(self.about_sidebar_link).to_be_visible(timeout=3000)

    def click_about_link(self):
        self.about_sidebar_link.click()