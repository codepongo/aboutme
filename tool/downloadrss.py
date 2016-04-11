#coding:utf-8
import os
import base64
import urllib
import pickle
import feedparser
import _dbhash as kvdb
import datetime
temp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
syndication = [
        ('http://codepongo.com/blog/feed', 'blog.rss', 'blog', 'static/blog.ico'),
        ('http://note.codepongo.com/feed', 'note.rss', 'diary', 'static/note.ico'),
        ('http://cook.codepongo.com/feed', 'cook.rss', 'cook', 'static/cook.ico'),
        #('http://www.douban.com/feed/people/zhuhuotui/interests', 'douban.rss', '豆瓣', 'static/douban.ico'),
        #('https://github.com/codepongo.atom', 'github.rss', 'GitHub', 'static/github.ico'),
        #('http://www.v2ex.com/feed/member/codepongo.xml', 'v2ex.rss', 'v2ex', 'static/v2ex.ico')
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
    max_len = 5
    max_len = size if len(rss_doc['items']) < 5 else 5
    channel['items'] = []
    for i in rss_doc['items']:
        item = {}
        item['title'] = i['title'].replace('<h1>', '').replace('</h1>', '')
        item['date'] = i['updated']
        item['url'] = i['link']
        channel['items'].append(item)
    return channel

def main():
    if not os.path.isdir(temp):
        os.mkdir(temp)
    rss = []
    for s in syndication:
        f = feed(s[0])
        rss.append(parse(f))
    
    with open(os.path.join(temp, 'rss'), 'wb') as f:
        pickle.dump(rss, f)

if __name__ == '__main__':
    exit(main())
