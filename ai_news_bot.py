import requests
from datetime import datetime

url = "https://hn.algolia.com/api/v1/search?query=AI"

response = requests.get(url).json()
articles = response["hits"][:5]

today = datetime.utcnow().strftime("%Y-%m-%d")

with open("ai_news.md", "w") as f:
    f.write(f"# AI News {today}\n\n")
    for article in articles:
        title = article["title"]
        link = article["url"]
        f.write(f"- [{title}]({link})\n")
