#coding:utf-8
import os
import base64
import urllib
import pickle
import feedparser
try:
    import dbhash as kvdb
except:
    import _dbhash as kvdb
import datetime
temp = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp')
syndication = [
        'http://codepongo.com/blog/feed',
        'http://note.codepongo.com/feed',
        'http://cook.codepongo.com/feed',
        'https://www.douban.com/feed/people/zhuhuotui/interests',
        'https://github.com/codepongo.atom', 
]

def feed(url):
    fn = base64.b64encode(url)
    fn = os.path.join(temp, fn)
    now = datetime.date.today()
    d = kvdb.open(os.path.join(temp, 'update'), 'c')
    if d.has_key(url) and d[url] == str(now):
        return fn

    with open(fn, 'wb') as f:
        rep = urllib.urlopen(url)
        f.write(rep.read())
    d[url] = str(now)
    return fn

def parse(f):
    channel = {}
    rss_doc = feedparser.parse(f)
    channel['url'] = rss_doc.feed.link
    length = 5
    length = size if len(rss_doc['items']) < 5 else 5
    channel['items'] = []
    for i in rss_doc['items']:
        if length < 0:
            break
        item = {}
        item['title'] = i['title']
        item['date'] = i['updated']
        item['url'] = i['link']
        channel['items'].append(item)
        length -= 1
    return channel

def main():
    if not os.path.isdir(temp):
        os.mkdir(temp)
    rss = []
    for s in syndication:
        f = feed(s)
        rss.append(parse(f))
    
    with open(os.path.join(temp, 'rss'), 'wb') as f:
        pickle.dump(rss, f)

if __name__ == '__main__':
    exit(main())
