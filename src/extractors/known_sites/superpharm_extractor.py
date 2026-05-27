class SuperPharmExtractor:
    def extract(self, page, url):
        page.goto(url)

        price = page.locator(".item-box.initialized").first.get_attribute("data-price")
        discount_price = page.locator(".item-box.initialized").first.get_attribute("data-discountprice")

        return {
            "site": "Super-Pharm",
            "url": url,
            "price": price,
            "discount_price": discount_price,
        }