from .playwright_adapter import PlaywrightAdapter

class EverlaneAdapter(PlaywrightAdapter):
    def __init__(self, headless = True):
        super().__init__(headless)

        # This is Aritizia's img locator, save for later
        # self.img_locator = '//div[@data-componentname="ImageGallery"]//a'
        self.img_locator = '//div[contains(@class, "product__media")]//img'

    async def _extract_image_url(self, page):
        img_url = None
        try:
            img_locator = page.locator(self.img_locator)
            if await img_locator.count() > 0:
                img_url = await img_locator.first.get_attribute("src")
                return img_url.lstrip("//")
        except Exception as e:
            print(f"Failed to find image url: {str(e)[:50]}")
        return img_url

    async def scrape(self, url, browser_type="chromium"):
        return await super().scrape(url, browser_type)