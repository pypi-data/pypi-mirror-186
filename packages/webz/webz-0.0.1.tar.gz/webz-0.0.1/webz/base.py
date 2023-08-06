#coding=utf-8

import sys
def bind(port=8080, ip= '127.0.0.1'):
    sys.argv[1:]=[ip+":"+str(port)]
    print("argv:",sys.argv)

pass

import web
class WebApplication(web.application):
    def run(self, port=8080, ip='0.0.0.0', *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, (ip, port))

pass
rurls = []

class SimpleRedirect:
    def run(self):
        urls = (
            '/(.*)', 'SimpleRedirect',
        )
        print("[SimpleRedirect] Server Init on:", self.port, self.ip, "to", self.url)
        app = WebApplication(urls, globals())
        app.run(port = self.port, ip = self.ip)
        print("[SimpleRedirect] Server Run")
    def __init__(self, url="", port=8080, ip = '127.0.0.1'):
        self.url = url
        self.port = port
        self.ip = ip
        rurls.append(url)
    def GET(self, url):
        print("[REDIRECT]: ", url, "TO", rurls[0])
        s = """
        <html>
        <head>
        <meta http-equiv="refresh" content="1,url=%s">
        </head>
        <body></body></html>
        """
        return s%(rurls[0],)
    def POST(self, url):
        return self.GET(url)

pass
def _redirect(port, url):
    obj = SimpleRedirect(url, port)
    obj.run()

pass
def redirect(port, url):
    import multiprocessing
    p = multiprocessing.Process(target = _redirect,args = [port, url])
    p.daemon = True
    p.start()

pass