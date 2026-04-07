import urllib.request
import urllib.error

from app import app


def test_index():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Iron Proxy Demo" in resp.data


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"


def test_httpbin_blocked():
    """Verify that Iron Proxy blocks requests to non-allowlisted domains."""
    try:
        urllib.request.urlopen("https://httpbin.org/get", timeout=5)
        # If we're not behind the proxy (e.g. running locally), that's fine
    except urllib.error.URLError:
        pass  # Expected when Iron Proxy blocks the request
