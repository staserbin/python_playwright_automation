import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Page

from pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption(
        "--enable-tracing",
        action="store_true",
        default=False,
        help="Enable Playwright tracing",
    )

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser, request):
    # Create a new browser context for test isolation
    context = browser.new_context()

    # Check if tracing is enabled via the CLI option
    enable_tracing = request.config.getoption("--enable-tracing")

    trace_path = None
    if enable_tracing:
        # Create the directory reports/traces if it doesn't exist
        trace_dir = Path("reports/traces")
        trace_dir.mkdir(parents=True, exist_ok=True)

        # Start tracing with screenshots, DOM snapshots, and source code
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        # Build the full path for the trace file using the test name
        trace_name = request.node.name
        trace_path = trace_dir / f"{trace_name}.zip"

    # Create a new page for the test
    page = context.new_page()
    yield page  # Provide the page to the test function

    # Stop tracing and save the trace file if enabled
    if enable_tracing and trace_path:
        context.tracing.stop(path=str(trace_path))
        print(f"\nTracing saved to: {trace_path}")

    # Clean up after the test
    page.close()
    context.close()

@pytest.fixture()
def home_page(page: Page):
    home = HomePage(page)
    home.goto()
    return home