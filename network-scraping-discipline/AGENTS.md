# Network scraping discipline
- When fetching data from the same host repeatedly, add moderate randomized sleeps once there are more than three consecutive requests to that host. Avoid tight loops, high parallelism, and one-by-one bulk scraping patterns that can trigger rate limits or blocks.
- Prefer batch, aggregate, cached, or official data-center endpoints over per-item scraping when collecting data or processing large datasets.
- If any host or endpoint appears rate-limited, blocked, or unstable, report it promptly with the host, endpoint family, and observed error such as HTTP status, timeout, DNS failure, or connection reset. Then stop escalating request volume against that host unless the user explicitly approves a safer retry strategy.
