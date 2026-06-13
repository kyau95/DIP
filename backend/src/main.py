import sys
import os

# Add src directory to Python path before imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Move these to a separate file when parsing to insert into the DB
from scrapers.adapter import BaseAdapater, PlaywrightAdapter
from sqlalchemy import select
from urllib.parse import urlparse
from database.models import Product, PriceHistory
from database import SessionLocal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.products import router as product_router

app = FastAPI()
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    product_router,
    prefix="/api"
)

if __name__ == "__main__":
    base = BaseAdapater()
    play_adapter = PlaywrightAdapter()
    urls = [
        # "https://www.everlane.com/products/womens-court-sneaker-white-grass-green?variant=42973788078166",
        # "https://www.newegg.com/msi-rtx-5060-ti-8g-ventus-3x-oc-geforce-rtx-5060-ti-8gb-graphics-card-triple-fans/p/N82E16814982007",
        # "https://www.walmart.com/ip/GameSir-T7-Wired-Controller-Xbox-Series-X-S-Xbox-One-Windows-10-11-Plug-Play-Gaming-Gamepad-Hall-Effect-Joysticks-Hall-Trigger-White-Version/9374812633?classType=VARIANT&adsRedirect=true",
        # "https://www.target.com/p/audio-technica-ath-wp900-on-ear-headphones-flamed-maple/-/A-1001263584#lnk=sametab"
    ]
    
    # db = SessionLocal()
    
    # for url in urls:
    #     retailer_name = urlparse(url).hostname.split(".")[1]
    #     print(retailer_name)
                
        # print(play_adapter.scrape(url))
        # ret = base.scrape(url)
        
        # # Test insert
        # # When adding a product, have to add the price at the same time 
        # try:
        #     product = Product(
        #         retailer=retailer_name,
        #         product_name=ret["product_name"],
        #         product_url=url
        #     )
        #     db.add(product)
        #     db.commit()
        #     db.refresh(product)

        #     ph = PriceHistory(
        #         price=ret["price"],
        #         product_id=product.id,
        #         currency="usd",
        #     )
        #     db.add(ph)
        #     db.commit()
        #     db.refresh(ph)
        # except Exception as e:
        #     print(e)
        
    # # Test select
    # stmt = select(Product)
    # products = db.scalars(stmt).all()
    
    # for p in products:
    #     print(p)
        
    # stmt = select(PriceHistory)
    # phs = db.scalars(stmt).all()
    
    # for ph in phs:
    #     print(ph)
    
    # db.close()