from pytrends.request import TrendReq
from datetime import datetime
import os

today = datetime.now().strftime('%Y-%m-%d')
filename = f"trends/{today}.html"

# 관심 있는 키워드 리스트 직접 지정
keywords = ['AI', 'Bitcoin', 'ChatGPT', 'Taylor Swift', 'Elon Musk']

pytrends = TrendReq(hl='en-US', tz=540)
pytrends.build_payload(keywords, timeframe='now 7-d', geo='US')  # 미국 기준
df = pytrends.interest_over_time()

html = f"<html><head><meta charset='utf-8'><title>{today} 트렌드</title></head><body>"
html += f"<h2>📈 {today} 키워드 트렌드 (미국 기준)</h2><ul>"

# 평균 관심도 기준으로 정렬
average_trend = df[keywords].mean().sort_values(ascending=False)
for keyword, score in average_trend.items():
    html += f"<li>{keyword}: 평균 관심도 {score:.2f}</li>"

html += "</ul><p>실시간 트렌드를 기반으로 자동 생성된 키워드입니다.</p></body></html>"

os.makedirs("trends", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
