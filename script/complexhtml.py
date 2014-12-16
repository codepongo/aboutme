import HTMLParser
import basesixtyfour
import re
import os
try:
    import conf
    resume_path = conf.resume_path
except:
    resume_path = os.path.dirname(__file__)

def allfilesin1(template, out):
    with open(template, 'rb') as i:
        html = i.read()

    with open(out, 'wb') as index:
        index.write(allin1(html))

def allin1(html):
    class Parser(HTMLParser.HTMLParser):
        def __init__(self):
            self.icons = {}
            HTMLParser.HTMLParser.__init__(self)
        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                    for k, v in attrs:
                        if k == 'src':
                            file_path = os.path.join(resume_path, v)
                            if not os.path.isfile(file_path):
                                file_path = os.path.join('templates', v)

                            self.icons[v] = basesixtyfour.encode(file_path)

    p = Parser()
    p.feed(html)
    for key, value in p.icons.iteritems():
        html = html.replace('src="'+key+'"', 'src="data:image/x-icon;base64,'+value+'"')
    return html

if __name__ == '__main__':
    allfilesin1('templates/aboutme.standard.html', 'templates/aboutme.html')
    allfilesin1('templates/resume.standard.html', 'templates/resume.html')
