import requests
from playwright.sync_api import sync_playwright
from src.router.extractor_router import get_extractor_for_url


url = "http://localhost:8080"

params = {
    "q": "חיתולים",
    "format": "json"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.headers.get("Content-Type"))
print(response.text[:500])


data = response.json()

for result in data["results"][:10]:
    print(result["title"])
    print(result["url"])
    print()

url = data["results"][0]["url"]


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    for result in data["results"][:10]:
        url = result["url"]

        extractor = get_extractor_for_url(url)

        if extractor is None:
            print("No extractor for ", url)
            continue

        product_data = extractor.extract(page, url)
        print(product_data)

