import time
from playwright.sync_api import sync_playwright
from scrapers.adapter.base import BaseAdapater

class PlaywrightAdapter(BaseAdapater):
    def __init__(self):
        super().__init__()
    
    def scrape(self, url, browser_type="chromium", timeout=30000):
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
                browser_launcher = playwright.chromium if browser_type == "chromium" else playwright.firefox
                browser = browser_launcher.launch(
                    headless=True,
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
                price_selectors = [
                    "//span[contains(text(), '$')]",
                    "[class*='price' i]",
                    "[data-seo-id='hero-price']",
                    ".price",
                    "[class*='Cost']",
                ]
                
                found_price = None
                for selector in price_selectors:
                    try:
                        locator = page.locator(selector)
                        if locator.count() > 0:
                            found_price = locator.first.inner_text(timeout=5000)
                            print(f"Found price with selector '{selector}': {found_price}")
                            break
                    except Exception as e:
                        print(f"Selector '{selector}' failed: {str(e)[:50]}")
                        continue
                
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
                    "title": page_title,
                    "status": "success" if found_price else "passed_with_exception"
                }
        
        except Exception as e:
            print(f"\nJob failed: {str(e)}")
            return {
                "url": url,
                "price": None,
                "error": str(e),
                "status": "error"
            }

