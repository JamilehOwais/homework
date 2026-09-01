from playwright.sync_api import Page, expect


class LoginPage:
    
    # 1. Initialize the page and locators ONCE
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']") 

    # 2. Action: Navigate to the page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
        # Spaced Repetition: Using expect to ensure the page is ready
        expect(self.login_button).to_be_visible(timeout=5000)

    # 3. Action: Perform the login
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()