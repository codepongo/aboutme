import sys
import os
sys.path.append(os.path.dirname(__file__))
import web
import about
import resume
urls = (
    '/', about.me,
    '/resume/login', resume.authentication,
    '/resume(.pdf)', resume.download,
    '/resume(.docx)', resume.download,
    '/resume(.txt)', resume.download,
    '/resume.*', resume.view,
    '.*', about.me,
)

def error():
    return web.seeother('/')

app = web.application(urls, globals())
web.config.session_parameters['timeout'] = 5 * 60 #five minutes
if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'authentication': False})
    web.config._session = session
else:
    session = web.config._session

if web.config.get('_render') is None:
    web.config._render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))

if __name__ == '__main__':
    web.config.debug = True
    app.run()
else:
    app.internalerror = error
    app.notfound = error
    application = app.wsgifunc()
