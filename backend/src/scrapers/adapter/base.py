import re
import requests

from bs4 import BeautifulSoup


class BaseAdapter:
    def __init__(self):
        self.header = {
            "User-Agent": (
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36" 
            )
        }
        # Common price indicators used across websites
        self.price_indicators = [
            "price", "cost", "amount", "total", "value", 
            "product-price", "item-price", "sale-price", "final-price"
        ]
        # Price regex pattern supporting $, €, £ and various formats
        self.price_pattern = r"[$€£]\s*\d+(?:[.,]\d{2})?|\d+(?:[.,]\d{2})?(?:\s*[$€£])"
        self.currency_symbols = r"[\$€£¥]"
        self.image_url_pattern = r"src=\".*\""

    def _find_price_element(self, soup: BeautifulSoup) -> str | None:
        """
        Generically searches for price elements using multiple strategies.
        Returns the first price found or None.
        """
        # Search by common class names
        for indicator in self.price_indicators:
            element = soup.find(class_=indicator)
            if element:
                price = re.search(self.price_pattern, element.get_text())
                if price:
                    return price.group(0)
        
        # Search by data attributes
        for indicator in self.price_indicators:
            elements = soup.find_all(attrs={"data-price": True})
            for element in elements:
                price = re.search(self.price_pattern, element.get_text())
                if price:
                    return price.group(0)
        
        # Search all text for price pattern
        all_text = soup.get_text()
        price = re.search(self.price_pattern, all_text)
        if price:
            return price.group(0)
        
        return None
    
    
    def _find_product_name(self, soup: BeautifulSoup) -> str | None:
        """
        Product names are usually always an h1 tag
        Find the first h1 element and return it otherwise None
        """
        elem = soup.find("h1")
        if elem:
            return elem.get_text().strip()
        return None

    def _find_image_url(self, soup: BeautifulSoup) -> str | None:
        """
        Finds the image url for the product
        This is a very rudimentary implementation though and likely will
        scrape the incorrect url as it finds the first img tag available
        from the top of the DOM
        """
        elem = soup.find("img")
        src_url = re.search(self.image_url_pattern, str(elem))
        if src_url:
            src_url = src_url.group(0).lstrip("src=//").replace("\"", "")
        return src_url

    def _fetch_soup(self, url: str) -> BeautifulSoup:
        """
        Fetches the HTML content from the URL and returns a parsed BeautifulSoup object.
        """
        response = requests.get(url, headers=self.header, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def _parse_price(self, price: str | None) -> tuple[str | None, str | None]:
        """
        Parses raw price text to extract the numeric price and currency symbol.
        """
        if not price:
            return None, None
        
        currency = None
        currency_match = re.search(self.currency_symbols, price)
        if currency_match:
            currency = currency_match.group(0)
        
        cleaned_price = re.sub(self.currency_symbols, "", price).strip()
        return cleaned_price, currency

    def _extract_data(self, soup: BeautifulSoup, url: str) -> dict:
        """
        Extracts product name, price, currency, and image URL from the parsed BeautifulSoup soup.
        """
        raw_price = self._find_price_element(soup)
        price, currency = self._parse_price(raw_price)
        image_url = self._find_image_url(soup)
        product_name = self._find_product_name(soup)
        
        return {
            "url": url,
            "image_url": image_url,
            "price": price,
            "currency": currency,
            "product_name": product_name,
            "status": "success" if price else "no_price_found",
            "error": None
        }

    def scrape(self, url: str) -> dict:
        """
        Generic implementation:
            Scrapes price from target URL using multiple strategies.
            Searches for common price indicators and patterns.
            Returns a dictionary with price, status, and error information.
        """
        try:
            soup = self._fetch_soup(url)
            return self._extract_data(soup, url)
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
            return {
                "url": url,
                "image_url": None,
                "price": None,
                "currency": None,
                "product_name": None,
                "status": "error",
                "error": str(e)
            }