from playwright.sync_api import Page
import pytest

url_dict = {
    'playwright': 'https://playwright.dev/'
}


@pytest.fixture(scope='session')
def load_url_playwright(page: Page):
    page.goto(url_dict['playwright'])
    return page
