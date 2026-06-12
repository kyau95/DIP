import re
import requests

from bs4 import BeautifulSoup


class BaseAdapater:
    def __init__(self):
        self.header = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            )
        }
        # Common price indicators used across websites
        self.price_indicators = [
            "price", "cost", "amount", "total", "value", 
            "product-price", "item-price", "sale-price", "final-price"
        ]
        # Price regex pattern supporting $, €, £ and various formats
        self.price_pattern = r"[$€£]\s*\d+(?:[.,]\d{2})?|\d+(?:[.,]\d{2})?(?:\s*[$€£])"

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
        

    def scrape(self, url: str) -> dict:
        """
        Generic implementation:
            Scrapes price from target URL using multiple strategies.
            Searches for common price indicators and patterns.
            Returns a dictionary with price, status, and error information.
        """
        try:
            response = requests.get(url, headers=self.header, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            price = self._find_price_element(soup)
            product_name = self._find_product_name(soup)
            return {
                "url": url,
                "price": price,
                "product_name": product_name,
                "status": "success" if price else "no_price_found",
                "error": None
            }
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
            return {
                "url": url,
                "price": None,
                "product_name": None,
                "status": "error",
                "error": str(e)
            }