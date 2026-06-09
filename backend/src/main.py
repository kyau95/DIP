from scrapers.adapter.base import BaseAdapater


if __name__ == "__main__":
    base = BaseAdapater()
    
    urls = [
        "https://www.everlane.com/products/womens-court-sneaker-white-grass-green?variant=42973788078166",
        "https://www.newegg.com/msi-rtx-5060-ti-8g-ventus-3x-oc-geforce-rtx-5060-ti-8gb-graphics-card-triple-fans/p/N82E16814982007",
        "https://www.walmart.com/ip/GameSir-T7-Wired-Controller-Xbox-Series-X-S-Xbox-One-Windows-10-11-Plug-Play-Gaming-Gamepad-Hall-Effect-Joysticks-Hall-Trigger-White-Version/9374812633?classType=VARIANT&adsRedirect=true",
        "https://www.target.com/p/audio-technica-ath-wp900-on-ear-headphones-flamed-maple/-/A-1001263584#lnk=sametab"
    ]
    for url in urls:
        print(base.scrape(url))