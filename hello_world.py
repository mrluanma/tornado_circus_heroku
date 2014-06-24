import socket

import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.options import define, options, parse_command_line


define("fd", default=None, help="File Descriptor given by circus", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


application = tornado.web.Application([
    (r"/", MainHandler),
])


def main():
    parse_command_line()
    sock = socket.fromfd(options.fd, socket.AF_UNIX, socket.SOCK_STREAM)
    server = HTTPServer(application)
    server.add_socket(sock)
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
