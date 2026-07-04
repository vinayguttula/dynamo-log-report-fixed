import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_is_valid_json():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    assert REPORT.exists(), "report.json not found"
    with open(REPORT) as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json root is not a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the actual number of requests in the log."""
    with open(REPORT) as f:
        data = json.load(f)
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips equals the actual number of distinct client IPs."""
    with open(REPORT) as f:
        data = json.load(f)
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Criterion 4: top_path equals the request path with the highest frequency."""
    with open(REPORT) as f:
        data = json.load(f)
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
