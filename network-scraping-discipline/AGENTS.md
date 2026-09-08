# Network scraping discipline

- After more than three consecutive requests to the same host, add moderate randomized waits; avoid tight loops, high concurrency, and large per-item scraping runs. Prefer batch, aggregate, cached, or official endpoints for large-scale data analysis.
- On rate limits, blocks, or instability, report the host, endpoint scope, and specific error (status code, timeout, DNS, connection reset, etc.); stop increasing requests to that host unless the user approves a safer retry strategy.
