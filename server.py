# from BaseHTTPServer import BaseHTTPRequestHandler
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse as urlparse
import string,cgi,time
from os import curdir, sep
from my_inverted_index import display_results

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        
        if self.path=="/":
            self.path="/views/index.html"

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".svg"):
                mimetype='image/svg+xml'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".ttf"):
                mimetype='application/x-font-ttf'
                sendReply = True
            if self.path.endswith(".otf"):
                mimetype='application/x-font-opentype'
                sendReply = True
            if self.path.endswith(".woff"):
                mimetype='application/font-woff'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rt')
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
                print(curdir + sep + self.path)

            elif (len(self.path.split('=')) == 2)  :
                mimetype = 'text/html'
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                print("hello world")
                q = self.path.split('=')[1]
                q = q.replace("%20"," ")
                result = display_results(q)
                c = "";
                for a in result:
                    for b in a:
                        c = c +"," +b
                self.wfile.write(c.encode('utf-8'))
                print(curdir + sep + self.path)
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):

        if self.path=="/run":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
            })


                        #self.send_response(200)
                        #self.end_headers()
            return
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()