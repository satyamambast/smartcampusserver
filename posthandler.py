from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import mysql.connector
class DB:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="root", database="smartdustbin")
        self.mycursor = self.mydb.cursor()
    def inserttodustbin(self,id,perc):
        update_query="""UPDATE data SET per==%s where id='%s'"""
        update_tuple=(perc,id)
        self.mycursor.execute(update_query,update_tuple)
        self.mydb.commit()
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.DaBa=DB()
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself)
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        post_data=post_data.decode('utf-8')
        d = dict(x.split("=") for x in post_data.split("&"))
        if d["type"]=="update":
            self.DaBa.inserttodustbin(d["id"],d["percentage"])



def run(server_class=HTTPServer, handler_class=S, port=8090):
    logging.basicConfig(level=logging.INFO)
    server_address = ('',port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
