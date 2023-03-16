import feedparser, time

blog_url = "https://cookie-dev.tistory.com/rss"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{time.strftime('%Y/%m/%d', feed_date)} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
## 기존의 README.md 내용
"""
resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
