# Sales Tracker but make it with Microservices

## Design Summary
Take a web scraping API `(Playwright)`, scrape a website of your choice and a product from that website.</br>
Examples:
- Amazon
- Newegg
- Bestbuy
- Target
- Walmart 

Track that item's price and receive a notification if it ever drops below a desired value or if that price changes in some way. Store that tracked item in a Postgres database because we need it.

Attach a UI to it, React or Svelte (idk which one yet). React if basic, Svelte for fun.

Containerize the project in Docker for consistent environments.

Your `.env` file needs to contain the `DB_URL` and a `DEBUG` flag 

Example `.env` config
```conf
DB_URL=postgresql+psycopg://postgres:<db pass>@localhost:<port>/<database name>
DEBUG=0

Default DB port is 5432
DEBUG flag can be any value other than zero to toggle it on and off
```

---

### Phase 1: Build the Scraper app in Playwright
```
                        Scraper Orchestrator
                                │
      ┌────────────────────────────────────────────────────┐
      │                 │                 │                │
      ▼                 ▼                 ▼                ▼
 AmazonAdapter   WalmartAdapter   BestBuyAdapter     DefaultAdapter
 ```


```
                     ┌──────────────┐
                     │  Svelte UI   │
                     └──────┬───────┘
                            │
                            ▼
                    ┌────────────────┐
                    │  FastAPI API   │
                    └──────┬─────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
    Product Mgmt      Scrape Jobs      User Alerts
                           │
                           ▼
                 ┌─────────────────┐
                 │ PostgreSQL      │
                 └─────────────────┘

                           │
                           ▼
                 ┌─────────────────┐
                 │ Playwright      │
                 │ Scraper Service │
                 └─────────────────┘
```

Relational database diagram
```
products
   │
   ├───────────────┐
   │               │
   ▼               ▼
price_history    alerts
   │
   ▼
scrape_jobs
```


### Phase 2: Attach a UI to the app
<<<<<<< Updated upstream
Feedback given was to make it more display focused, as you won't remember exactly what items were saved. 

So we want to show cards of the items and the associated price that has been scraped and saved to the UI.

```
┌───────────┬──────────┐
│           │          │ 
│    Image  │   Image  │
│   Item 1  │  Item 2  │
│     $$    │   $$$    │
│           │          │ 
├───────────┼──────────┤
│           │          │ 
│    Image  │   Image  │
│   Item 3  │  Item 4  │
│     $$    │   $$$    │
│           │          │
└───────────┴──────────┘
```
=======
We need to setup the FastAPI endpoints for each route

Potential routes:
- products `<---`
- price_history `<-- These two are the most important`
- health
- alerts
- scrape_job
>>>>>>> Stashed changes

### Phase 3: Containerize it in Docker

## Architecture 
```
React Dashboard
       ↓
API Gateway
       ↓
 ┌──────────────┐
 │ API Service  │
 └──────────────┘

       ↓

Kafka/RabbitMQ

 ┌─────────┬──────────┬─────────────┐
 ↓         ↓          ↓
Scraper  Processor  Notification
Service   Service     Service

       ↓
PostgreSQL

       ↓
Analytics Service

Monitoring:
Prometheus
Grafana
Loki

Deployment:
GitHub Actions
ArgoCD
Kubernetes
```