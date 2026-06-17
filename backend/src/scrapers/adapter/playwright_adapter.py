import re

from playwright.sync_api import sync_playwright
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
    
    def scrape(self, url, browser_type="chromium"):
        """
        Scrape a URL using Playwright with anti-detection and JS rendering support.
        
        Args:
            url: Target URL to scrape
            browser_type: "chromium" or "firefox"
            timeout: Wait timeout in milliseconds (default 30s)
        
        Returns:
            Dictionary with scraped data or error info
        """
        try:
            with sync_playwright() as playwright:
                browser_launcher = playwright.chromium if \
                    browser_type == "chromium" else playwright.firefox
                browser = browser_launcher.launch(
                    headless=self.headless,
                    args=["--disable-blink-features=AutomationControlled"],
                )                
                context = browser.new_context(
                    user_agent=self.header["User-Agent"],
                    viewport={"width": 1280, "height": 720},
                    extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
                )
                
                page = context.new_page()
                print(f"Navigating to {url}...")
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=15000)
                except:
                    print("Initial load timeout, continuing anyway...")
                page.wait_for_timeout(3000)
                
                found_price = None
                found_currency = None
                for selector in self.price_selectors:
                    try:
                        locator = page.locator(selector)
                        if locator.count() > 0:
                            price_text = locator.first.inner_text(timeout=5000)
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
                
                # Find product name from h1 tag
                product_name = None
                try:
                    h1_locator = page.locator("h1")
                    if h1_locator.count() > 0:
                        product_name = h1_locator.first.inner_text(timeout=5000)
                        print(f"Found product name: {product_name}")
                except Exception as e:
                    print(f"Failed to find h1 tag: {str(e)[:50]}")
                
                page_title = page.title()
                page_url = page.url
                
                # Debug
                if not found_price:
                    print("No price found. Dumping page HTML for debugging...")
                    content = page.content()
                    print(f"Page title: {page_title}")
                    print(f"Page URL: {page_url}")
                    if "<body" in content:
                        body_start = content.index("<body")
                        print(content[body_start:body_start+500])
                browser.close()
                
                return {
                    "url": url,
                    "price": found_price,
                    "currency": found_currency,
                    "product_name": product_name,
                    "status": "success" if found_price else "no_price_found",
                    "error": None
                }
        
        except Exception as e:
            print(f"\nJob failed: {str(e)}")
            return {
                "url": url,
                "price": None,
                "currency": None,
                "product_name": None,
                "status": "error",
                "error": str(e)
            }