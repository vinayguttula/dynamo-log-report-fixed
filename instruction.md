You have an Apache-style access log at `/app/access.log`. Parse it and produce a JSON report at `/app/report.json`.

The report must be a single JSON object with exactly these keys:

- `total_requests` — integer, the total number of log lines (excluding blanks).
- `unique_ips` — integer, the count of distinct client IP addresses.
- `top_path` — string, the request path that appears most often.

Success criteria:

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` equals the actual number of requests in the log.
3. `unique_ips` equals the actual number of distinct client IPs in the log.
4. `top_path` equals the request path with the highest frequency.
