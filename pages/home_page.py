import allure
from playwright.sync_api import Page, expect
from utils.text_utils import clean_text


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://automationexercise.com/"
        self.top_menu = page.locator("ul.nav.navbar-nav > li > a")

    @allure.step("Navigate to the page URL")
    def goto(self):
        self.page.goto(self.url)
        return self

    @allure.step("Check if 'Home' menu item is selected (highlighted in orange)")
    def is_home_selected(self):
        return self.page.get_by_role("link", name="Home").get_attribute("style") == "color: orange;"

    @allure.step("Verify that the carousel is visible on the page")
    def is_carousel_visible(self):
        expect(self.page.locator(".carousel-inner").first).to_be_visible()

    @allure.step("Check that the Features Items title is present")
    def has_features_title(self):
        expect(self.page.locator("div.features_items h2[class*='title']")).to_contain_text("Features Items")

    @allure.step("Get list of top menu items")
    def get_menu_items(self) -> list[str]:
        return [clean_text(item.inner_text()) for item in self.top_menu.all()]