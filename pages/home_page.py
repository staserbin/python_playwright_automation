from playwright.sync_api import Page, expect
from utils.text_utils import clean_text


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://automationexercise.com/"
        self.top_menu = page.locator("ul.nav.navbar-nav > li > a")

    def goto(self):
        self.page.goto(self.url)
        return self

    def is_home_selected(self):
        return self.page.get_by_role("link", name="Home").get_attribute("style") == "color: orange;"

    def is_carousel_visible(self):
        expect(self.page.locator(".carousel-inner").first).to_be_visible()

    def has_features_title(self):
        expect(self.page.locator("div.features_items h2[class*='title']")).to_contain_text("Features Items")

    def get_top_menu_options(self) -> list[str]:
        return [clean_text(item.inner_text()) for item in self.top_menu.all()]