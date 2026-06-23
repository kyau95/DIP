from database.models import Product, PriceHistory
from schemas.product import ProductResponse
from scrapers.adapter import BaseAdapater, PlaywrightAdapter

from errors import PriceNotFoundException, UnsupportedRetailerException
from sqlalchemy.orm import Session
from urllib.parse import urlparse


async def create_product(
        url: str, 
        db: Session
    ):
    # Will need to account for dupe URLs in the future
    
    retailer_name = urlparse(url).hostname.split(".")[1]
    base, pw = BaseAdapater(), PlaywrightAdapter()
    
    for adapter in [base, pw]:
        if isinstance(adapter, PlaywrightAdapter):
            ret = await adapter.scrape(url)
        else:
            ret = adapter.scrape(url)
        
        if ret["price"] is not None:
            break
    
    from pprint import pprint
    pprint(ret)

    if ret["price"] is None:
        raise PriceNotFoundException()    
    product = Product(
        retailer=retailer_name,
        product_name=ret["product_name"],
        product_url=url,
    )    
    db.add(product)
    db.flush()
    
    history = PriceHistory(
        price=ret["price"],
        product_id=product.id,
        currency=ret["currency"]
    )    
    db.add(history)
    db.commit()
    db.refresh(product)
    
    return ProductResponse(
        id=product.id,  
        imageUrl="",
        price=ret["price"],
        currency=ret["currency"],
        productName=ret["product_name"],
        productUrl=url,
        retailer=product.retailer
    )