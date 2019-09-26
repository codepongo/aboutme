import sys
import os
import web
import pickle
temp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'temp')
class me:
    def GET(self):
        templates = os.path.join(os.path.dirname(__file__), 'templates')
        render = web.template.render(templates)
        rss = []
        rss_path = os.path.join(temp, 'rss')
        if os.path.isfile(rss_path):
            with open(os.path.join(temp, 'rss'), 'rb') as f:
                rss = pickle.load(f)
        return render.aboutme(rss)
