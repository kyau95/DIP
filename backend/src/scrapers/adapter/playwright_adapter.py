import re

from playwright.async_api import async_playwright
from scrapers.adapter.base import BaseAdapater

class PlaywrightAdapter(BaseAdapater):
    def __init__(self, headless: bool = True):
        super().__init__()
        self.price_selectors = [
            "//span[contains(text(), '$')] || //div[contains(text(), '$')]",
            ".price",
            "[class*='price' i]",
            "[class*='Cost']",
        ]
        self.headless = headless
    
    async def _setup_browser_and_page(self, playwright, browser_type: str):
        """
        Launches the browser and returns the browser instance and a new page.
        """
        browser_launcher = playwright.chromium if \
            browser_type == "chromium" else playwright.firefox
        browser = await browser_launcher.launch(
            headless=self.headless,
            args=["--disable-blink-features=AutomationControlled"],
        )                
        context = await browser.new_context(
            user_agent=self.header["User-Agent"],
            viewport={"width": 1280, "height": 720},
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
        )
        page = await context.new_page()
        return browser, page

    async def _navigate_to_url(self, page, url: str):
        """
        Navigates the page to the target URL.
        """
        print(f"Navigating to {url}...")
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=15000)
        except Exception as e:
            print(f"Initial load timeout, continuing anyway... {str(e)[:50]}")
        await page.wait_for_timeout(3000)

    async def _extract_price(self, page) -> tuple[str | None, str | None]:
        """
        Attempts to extract the price and currency using selectors.
        """
        found_price = None
        found_currency = None
        for selector in self.price_selectors:
            try:
                locator = page.locator(selector)
                if await locator.count() > 0:
                    price_text = await locator.first.inner_text(timeout=5000)
                    price_match = re.search(
                        self.price_pattern, 
                        price_text
                    )
                    if price_match:
                        found_price = price_match.group(0)
                        # Extract currency symbol before removing it
                        currency_match = re.search(self.currency_symbols, found_price)
                        if currency_match:
                            found_currency = currency_match.group(0)
                        # Remove currency symbol from price
                        found_price = re.sub(self.currency_symbols, "", found_price).strip()
                        print(f"Found price with selector '{selector}': {found_price} ({found_currency})")
                        break
            except Exception as e:
                print(f"Selector '{selector}' failed: {str(e)[:50]}")
                continue
        return found_price, found_currency

    async def _extract_product_name(self, page) -> str | None:
        """
        Attempts to extract the product name from the h1 element.
        """
        product_name = None
        try:
            h1_locator = page.locator("h1")
            if await h1_locator.count() > 0:
                product_name = await h1_locator.first.inner_text(timeout=5000)
                print(f"Found product name: {product_name}")
        except Exception as e:
            print(f"Failed to find h1 tag: {str(e)[:50]}")
        return product_name

    async def _extract_image_url(self, page) -> str | None:
        """
        Attempts to extract the image URL from img tags.
        """
        return None

    async def _dump_debug_info(self, page):
        """
        Dumps debug info if no price is found.
        """
        try:
            print("No price found. Dumping page HTML for debugging...")
            page_title = await page.title()
            page_url = page.url
            content = await page.content()
            print(f"Page title: {page_title}")
            print(f"Page URL: {page_url}")
            if "<body" in content:
                body_start = content.index("<body")
                print(content[body_start:body_start+500])
        except Exception as e:
            print(f"Failed to dump debug info: {str(e)[:50]}")

    async def scrape(self, url, browser_type="chromium"):
        """
        Scrape a URL using Playwright with anti-detection and JS rendering support.
        
        Args:
            url: Target URL to scrape
            browser_type: "chromium" or "firefox"
        
        Returns:
            Dictionary with scraped data or error info
        """
        try:
            async with async_playwright() as playwright:
                browser, page = await self._setup_browser_and_page(playwright, browser_type)
                try:
                    await self._navigate_to_url(page, url)
                    
                    found_price, found_currency = await self._extract_price(page)
                    product_name = await self._extract_product_name(page)
                    image_url = await self._extract_image_url(page)
                    
                    # Debug
                    if not found_price:
                        await self._dump_debug_info(page)
                        
                    return {
                        "url": url,
                        "image_url": image_url,
                        "price": found_price,
                        "currency": found_currency,
                        "product_name": product_name,
                        "status": "success" if found_price else "no_price_found",
                        "error": None
                    }
                finally:
                    await browser.close()
        except Exception as e:
            print(f"\nJob failed: {str(e)}")
            return {
                "url": url,
                "image_url": None,
                "price": None,
                "currency": None,
                "product_name": None,
                "status": "error",
                "error": str(e)
            }