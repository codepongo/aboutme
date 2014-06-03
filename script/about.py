import sys
import os
import feedparser
import downloadrss
import web

class me:
    def GET(self):
        templates = os.path.join(os.path.dirname(__file__), 'templates')
        render = web.template.render(templates)
        return render.aboutme(parse())

def parse():
    rss = []
    for r in downloadrss.rss:
        f = feedparser.parse(os.path.join(os.path.dirname(__file__), downloadrss.rssdir, r[1]))
        channel = {}
        channel['ico'] = r[3]
        channel['name'] = r[2]
        if f.feed.has_key('link'):
            channel['url'] = f.feed.link
        else:
            channel['url'] = ''
        channel['items'] = []
        if len(f['items']) < 10:
            size = len(f['items'])
        else:
            size = 10
        for i in range(0, size):
            item = {}
            item['title'] = f['items'][i]['title'].replace('<h1>', '').replace('</h1>', '')
            item['date'] = f['items'][i]['updated']
            item['url'] = f['items'][i]['link']
            channel['items'].append(item)
        rss.append(channel)
    return rss

if __name__ == '__main__':
    print parse()
