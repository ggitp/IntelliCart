from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://localhost:8080")

    browser.close()
