import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8000))

HTML = """<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Trading by Rahat V26</title>
<style>
body{margin:0;font-family:Arial;background:#0f172a;color:white;text-align:center;padding:20px}
.card{background:#1e293b;padding:20px;border-radius:15px;max-width:400px;margin:20px auto;box-shadow:0 0 20px rgba(0,0,0,0.5)}
h1{color:#facc15;font-size:28px}
.btn{background:#22c55e;color:white;border:none;padding:15px 25px;font-size:18px;border-radius:10px;width:100%;margin-top:10px;font-weight:bold}
.btn2{background:#3b82f6}
#result{font-size:32px;font-weight:bold;margin:20px 0;min-height:50px}
select{width:100%;padding:12px;border-radius:8px;font-size:16px;margin:10px 0}
.badge{background:#facc15;color:black;padding:5px 12px;border-radius:20px;font-size:13px;font-weight:bold}
</style>
</head>
<body>
<div class="card">
<div class="badge">TRADING BY RAHAT - V26 LIVE</div>
<h1>Trading by Rahat</h1>
<p>Quotex Signal - 1 Minute</p>
<select id="pair">
<option>EUR/USD</option><option>GBP/USD</option><option>USD/JPY</option><option>EUR/GBP</option><option>AUD/USD</option><option>USD/BDT</option>
</select>
<button class="btn" onclick="getSignal()">GET SIGNAL 🚀</button>
<div id="result">👆 চাপ দাও ভাই</div>
<p id="time"></p>
<button class="btn btn2" onclick="location.reload()">REFRESH</button>
<p style="font-size:12px;color:#94a3b8;margin-top:15px">Demo Signal Only - নিজের রিস্কে ট্রেড করো</p>
</div>
<script>
function getSignal(){
  var pairs = document.getElementById('pair').value;
  var r = Math.random();
  var sig = r > 0.5 ? '🟢 CALL - UP ⬆️' : '🔴 PUT - DOWN ⬇️';
  var col = r > 0.5 ? '#22c55e' : '#ef4444';
  var el = document.getElementById('result');
  el.innerHTML = pairs + '<br>' + sig;
  el.style.color = col;
  document.getElementById('time').innerHTML = 'Time: ' + new Date().toLocaleTimeString();
}
</script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))
    def log_message(self, format, *args):
        return

HTTPServer(('0.0.0.0', PORT), Handler).serve_forever()
