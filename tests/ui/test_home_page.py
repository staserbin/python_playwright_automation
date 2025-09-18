def test_home_page_is_opened(home_page):
    # Ensure that the 'Home' option on the top bar is orange
    assert home_page.is_home_selected()

    # Verify that the carousel banner is displayed
    home_page.is_carousel_visible()

    # Verify that the 'Features Items' title is displayed
    home_page.has_features_title()

def test_top_bar_options(home_page):
    expected_options = [
        "Home", "Products", "Cart", "Signup / Login", "Test Cases", "API Testing", "Video Tutorials", "Contact us"
    ]

    actual_options = home_page.get_top_menu_options()

    assert expected_options == actual_options, \
        f"Expected top bar titles: {expected_options}, but got: {actual_options}"
