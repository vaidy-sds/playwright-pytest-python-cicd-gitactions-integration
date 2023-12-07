from playwright.sync_api import Page, expect


def test_playwright_website(page: Page):
    # goto page
    page.goto("https://playwright.dev/")
    # check link on homepage
    expect(page.get_by_role("link", name="Playwright logo Playwright")).to_be_visible()
