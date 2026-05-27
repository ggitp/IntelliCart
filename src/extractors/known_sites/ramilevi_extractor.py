class RamiLevyExtractor:
    def extract(self, page, url):
        page.goto(url)

        product = page.locator(".product-flex").first

        name = product.locator(".inner-text.mt-2").first.inner_text()
        price = product.locator(".currency-product").first.inner_text()
        old_price_locator = product.locator(".old-price")

        if old_price_locator.count() > 0:
            discount_price = old_price_locator.first.inner_text()
        else :
            discount_price = None


        return {
            "name": name,
            "price": price,
            "discount_price": discount_price,
            "site": "RamiLevy",
            "url": url,

        }