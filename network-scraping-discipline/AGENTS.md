# Network scraping discipline

- After more than three consecutive requests to one host, add moderate randomized waits. Avoid tight loops, high concurrency, and per-item bulk scraping; prefer batch, aggregate, cached, or official data-center endpoints for large datasets.
- On rate limits, blocks, or instability, promptly report the host, endpoint family, and observed error (status code, timeout, DNS failure, connection reset, etc.). Stop increasing request volume against that host unless the user approves a safer retry strategy.
