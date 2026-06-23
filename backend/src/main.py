import sys
import os
import asyncio

# Add src directory to Python path before imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Move these to a separate file when parsing to insert into the DB
from scrapers.adapter import BaseAdapater, PlaywrightAdapter, EverlaneAdapter
from sqlalchemy import select
from urllib.parse import urlparse
from database.models import Product, PriceHistory
from database import SessionLocal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.products import router as product_router
from api.routes.price_history import router as price_history_router

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

for router in [product_router, price_history_router]:
    app.include_router(
        router,
        prefix="/api"
    )

if __name__ == "__main__":
    base = BaseAdapater()
    play_adapter = PlaywrightAdapter(False)
    e_adapter = EverlaneAdapter(False)
    urls = [
        # "https://www.everlane.com/products/womens-court-sneaker-white-grass-green?variant=42973788078166",
        # "https://www.newegg.com/msi-rtx-5060-ti-8g-ventus-3x-oc-geforce-rtx-5060-ti-8gb-graphics-card-triple-fans/p/N82E16814982007",
        # "https://www.walmart.com/ip/GameSir-T7-Wired-Controller-Xbox-Series-X-S-Xbox-One-Windows-10-11-Plug-Play-Gaming-Gamepad-Hall-Effect-Joysticks-Hall-Trigger-White-Version/9374812633?classType=VARIANT&adsRedirect=true",
        # "https://www.target.com/p/audio-technica-ath-wp900-on-ear-headphones-flamed-maple/-/A-1001263584#lnk=sametab",
        # "https://www.bestbuy.com/product/apple-airpods-pro-3-wireless-active-noise-cancelling-earbuds-with-heart-rate-sensing-feature-white/JJGCQLYK5F",
        # "https://www.amazon.com/NZXT-C850-Gold-Core-Cybenetics/dp/B0FQ69SSM9/?_encoding=UTF8&pd_rd_w=Kcplu&content-id=amzn1.sym.a9c4acee-9ca0-46be-bae3-532a2b4b0d29%3Aamzn1.symc.5a16118f-86f0-44cd-8e3e-6c5f82df43d0&pf_rd_p=a9c4acee-9ca0-46be-bae3-532a2b4b0d29&pf_rd_r=GGCN2HXQSHT2BJY4P21Z&pd_rd_wg=g0HZf&pd_rd_r=c65afec5-3650-49a8-af40-79e0c4d9c43a",
        # "https://shop.lululemon.com/p/unisex-find-your-balance-grip-quarter-socks/bp9lb8d0oa?color=33454",
        # "https://www.aritzia.com/us/en/product/etiquette-blazer/118278.html?color=11420",
        # "https://www.newegg.com/amd-ryzen-7-9000-series-ryzen-7-9800x3d-granite-ridge-zen-5-socket-am5-desktop-cpu-processor/p/N82E16819113877?Item=N82E16819113877",
        "https://www.everlane.com/products/womens-denim-chore-jacket-2-mid-indigo",
    ]
    
    db = SessionLocal()
    
    async def main():
        for url in urls:
            retailer_name = urlparse(url).hostname.split(".")[1]
            # ret = await play_adapter.scrape(url)
            # ret = base.scrape(url)
            # ret = await e_adapter.scrape(url)
            # print(ret)
            
            # # Test insert
            # if ret["price"] is not None:
            #     try:
            #         product = Product(
            #             retailer=retailer_name,
            #             product_name=ret["product_name"],
            #             product_url=url,
            #             image_url=ret["image_url"]
            #         )
            #         db.add(product)
            #         db.commit()
            #         db.refresh(product)

            #         ph = PriceHistory(
            #             price=ret["price"],
            #             product_id=product.id,
            #             currency=ret["currency"],
            #         )
            #         db.add(ph)
            #         db.commit()
            #         db.refresh(ph)
            #     except Exception as e:
            #         print(e)
            # else:
            #     print("Failed to scrape price")
    
    asyncio.run(main())
    # Test select
    # stmt = select(Product)
    # products = db.scalars(stmt).all()
    
    # for p in products:
    #     print(p)
        
    # stmt = select(PriceHistory)
    # phs = db.scalars(stmt).all()
    
    # for ph in phs:
    #     print(ph)
    
    db.close()