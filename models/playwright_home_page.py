from playwright.sync_api import Page, expect


class PlaywrightHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://playwright.dev/"
        self.playwright_logo = self.page.get_by_role("link", name="Playwright logo Playwright")

    def goto(self):
        self.page.goto(self.url)

    def check_logo(self):
        expect(self.playwright_logo).to_be_visible()
