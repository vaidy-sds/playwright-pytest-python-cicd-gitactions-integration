from playwright.sync_api import Page

from models.playwright_home_page import PlaywrightHomePage


def test_playwright_website(page: Page):
    # goto page
    homepage = PlaywrightHomePage(page)
    homepage.goto()

    # check link on homepage
    homepage.check_logo()
