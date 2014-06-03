#coding:utf-8
import os
import urllib2
rssdir = 'temp'
rss = [
        ('http://codepongo.com/blog/feed', 'blog.rss', 'blog', 'static/blog.ico'),
        ('http://note.codepongo.com/feed', 'note.rss', 'diary', 'static/note.ico'),
        ('http://cook.codepongo.com/feed', 'cook.rss', 'cook', 'static/cook.ico'),
        ('http://www.douban.com/feed/people/zhuhuotui/interests', 'douban.rss', '豆瓣', 'static/douban.ico'),
        ('https://github.com/codepongo.atom', 'github.rss', 'GitHub', 'static/github.ico'),
        ('http://www.v2ex.com/feed/member/codepongo.xml', 'v2ex.rss', 'v2ex', 'static/v2ex.ico')
]
def download(url, file):
    with open(os.path.join(rssdir, file), 'wb') as f:
        req = urllib2.Request(url)
        rep = urllib2.urlopen(req)
        f.write(rep.read())
        f.close()
def main():
    if not os.path.isdir(rssdir):
        os.mkdir(rssdir)
    for r in rss:
        print r[0]
        download(r[0], r[1])
    return 0

if __name__ == '__main__':
    exit(main())
