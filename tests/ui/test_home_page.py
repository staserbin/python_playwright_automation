import allure


class TestHomePage:

    @allure.title("Verify homepage loads on website launch")
    @allure.description("Validate that the main page (homepage) is the first page displayed when accessing the website")
    def test_home_page_is_opened(self, home_page):
        with allure.step("Ensure that the 'Home' option on the top bar is orange"):
            assert home_page.is_home_selected()

        with allure.step("Verify that the carousel banner is displayed"):
            home_page.is_carousel_visible()

        with allure.step("Verify that the 'Features Items' title is displayed"):
            home_page.has_features_title()

    @allure.title("Menu items validation")
    @allure.description("Validate that the menu of the main page contains all expected navigation items")
    def test_menu_items(self, home_page):
        expected_options = [
            "Home", "Products", "Cart", "Signup / Login", "Test Cases", "API Testing", "Video Tutorials", "Contact us"
        ]

        actual_options = home_page.get_menu_items()

        with allure.step("Verify that all expected menu items are displayed"):
            assert expected_options == actual_options, \
                f"Expected menu items: {expected_options}, but got: {actual_options}"
