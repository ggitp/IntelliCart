class BabySitterExtractor:
    def extract(self, page, url):
        page.goto(url)

        name = page.locator(".product-item__product-title").first.inner_text()
        price = page.locator("span.product-item__price").first.inner_text()

        return {
            "name": name,
            "Site": "Baby-Sitter",
            "url": url,
            "price": price,
            "discount_price": None
        }