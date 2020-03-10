from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import mysql.connector
# class DB:
#     def __init__(self):
#         self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="root", database="smartdustbin",port=3306)
#         self.mycursor = self.mydb.cursor()
#     def inserttodustbin(self,id,perc):
#         update_query="""UPDATE data SET per==%s where id='%s'"""
#         update_tuple=(perc,id)
#         self.mycursor.execute(update_query,update_tuple)
#         self.mydb.commit()
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="root", database="campus"        )
        self.mycursor = self.mydb.cursor()
        #self.mycursor.execute("SHOW DATABASE
        # self.DaBa=DB()
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
        if d["type"]=="nfc":
            select_query="""select credit from users where ID=%s"""
            self.mycursor.execute(select_query,d["ID"])
            deets=self.mycursor.fetchall()
            if len(deets)==0:
                insert_query = """INSERT INTO users
                                VALUES (%s, %s) """
                insert_tuple=(d[ID],1)
                self.mycursor.execute(insert_query,insert_tuple)
            else:
                cr=int(d[0][0])+1
                update_query="""UPDATE users SET credit=%s where ID=%s"""
            self.mydb.commit()
        if d["type"]=="update":
            for key in d:
                print(key)

            




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
