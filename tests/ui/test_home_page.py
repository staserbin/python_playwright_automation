from playwright.sync_api import expect


def test_example(page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Home").click()
    expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
