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



---

### Phase 1: Build the Scraper app in Playwright
```
                Scraper Orchestrator
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
 AmazonAdapter   WalmartAdapter   BestBuyAdapter
 ```


```
                     ┌──────────────┐
                     │   React UI   │
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


### Phase 2: Attach a UI to the app

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