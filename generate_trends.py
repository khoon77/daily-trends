from pytrends.request import TrendReq
from datetime import datetime
import os

today = datetime.now().strftime('%Y-%m-%d')
filename = f"trends/{today}.html"

pytrends = TrendReq(hl='ko', tz=540)
trending = pytrends.trending_searches(pn='south_korea')
popular = trending[0].tolist()

html = f"<html><head><meta charset='utf-8'><title>{today} 트렌드</title></head><body>"
html += f"<h2>🔥 {today} 구글 인기 키워드</h2><ul>"
for keyword in popular[:10]:
    html += f"<li>{keyword}</li>"
html += "</ul><p>자동 수집된 트렌드 키워드입니다.</p></body></html>"

os.makedirs("trends", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
