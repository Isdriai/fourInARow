#tcp_server_multi.py
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
	
	def handle(self):
		print('Got connection from', self.client_address)
		for line in self.rfile:
              self.wfile.write(line.upper())



if __name__ == '__main__':

	from threading import Thread #to serve max 16 clients
	NWORKERS = 16
	TCPServer.allow_reuse_address = True
	serv = TCPServer(('', 9999), EchoHandler)
	for n in range(NWORKERS):
	t = Thread(target=serv.serve_forever)
	t.daemon = True
	t.start()
	serv.serve_forever()