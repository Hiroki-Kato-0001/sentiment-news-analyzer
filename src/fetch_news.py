import feedparser

def get_headlines(limit=20):
    rss_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(rss_url)
    return [entry.title for entry in feed.entries[:limit]]
