from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iron Proxy Demo</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 600px; margin: 80px auto; padding: 0 20px; }
    h1 { color: #333; }
    .status { padding: 12px 20px; background: #e8f5e9; border-radius: 6px; }
  </style>
</head>
<body>
  <h1>Iron Proxy Demo</h1>
  <p class="status">Server is running.</p>
  <p>This app uses <a href="https://github.com/marketplace/actions/iron-proxy">Iron Proxy</a>
     in CI to enforce egress filtering.</p>
</body>
</html>"""


@app.route("/health")
def health():
    return {"status": "ok"}
