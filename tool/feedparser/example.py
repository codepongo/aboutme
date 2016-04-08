import feedparser
d = feedparser.parse('http://feed.cnblogs.com/blog/sitehome/rss')
print d['entries'][0]['content'][0]['value']
