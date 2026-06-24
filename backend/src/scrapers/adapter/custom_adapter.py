from .playwright_adapter import PlaywrightAdapter


class EverlaneAdapter(PlaywrightAdapter):
    def __init__(self, headless = True):
        super().__init__(headless)

        # This is Aritizia's img locator, save for later
        # self.img_locator = '//div[@data-componentname="ImageGallery"]//a'
        self.img_locator = '//div[contains(@class, "product__media")]//img'
        

class NeweggAdapter(PlaywrightAdapter):
    def __init__(self, headless = True):
        super().__init__(headless)
        
        self.price_locator = '//div[contains(@class, "price-current")]'
        self.img_selector = '//div[contains(@class, "swiper-zoom-container")]//img'