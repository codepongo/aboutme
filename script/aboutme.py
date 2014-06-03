import sys
import os
sys.path.append(os.path.dirname(__file__))
import web
import about
urls = ('.*', about.me,
)
app = web.application(urls, globals())
if __name__ == '__main__':
    app.run()
else:
    application = app.wsgifunc()
