from playwright.sync_api import Page, expect

def test_menu_navigation(logged_in_page: Page):
    # 1. Open side menu using accessible role locator
    logged_in_page.get_by_role("button", name="Open Menu").click()

    # 2. Click About link
    logged_in_page.get_by_role("link", name="About").click()

    # 3. Web-first assertion (auto-waits for URL redirect)
    expect(logged_in_page).to_have_url("https://saucelabs.com/")