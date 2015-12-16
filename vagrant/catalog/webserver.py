__author__ = 'abhig'

import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#sqlalchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem


#CRUD operations
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                message =''
                message+= "<html><body><h1>Restaurant Menu</h1><br>"
                message+= "<a href='/restaurants/new'> Create a New Restaurant</a><br><br>"
                restaurants = session.query(Restaurant)
                for restaurant in restaurants:
                    message += restaurant.name
                    message += "<br>"
                    message += "<a href ='/restaurants/%s/edit'>Edit</a><br>" % restaurant.id
                    message += "<a href = '/restaurants/%s/delete'>Delete</a><br>" %restaurant.id
                    message += "<br>"
                    print restaurant.name
                self.wfile.write(message)
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                message =''
                message += "<html><body><h1>Please Enter the Name of the Restaurant</h1>"
                message += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                message+= "<input name = 'newRestaurantName' type = 'text'><input type = 'submit' value = 'Create'><br>"
                message += "</form></body></html>"

                self.wfile.write(message)
                return

            if self.path.endswith("/edit"):
                restaurantIdPath = self.path.split("/")[2]
                if restaurantIdPath != []:
                    self.send_response(200)
                    self.send_header('content-type','text/html')
                    self.end_headers()
                    message =''
                    message += "<html><body>"
                    message += "<h1>Please Enter a New Name:</h1>"
                    message += "<form method = post enctype = 'multipart/form-data' action ='/restaurants/%s/edit'>"\
                               %restaurantIdPath
                    message += "<input name = 'updatedName' type = 'text' ><input type = 'submit' value ='Update'>"
                    message += "</form></html></body>"
                    self.wfile.write(message)
                    return

            if self.path.endswith("/delete"):
                restaurantIdPath = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIdPath).one()
                if restaurantIdPath != []:
                    self.send_response(200)
                    self.send_header('content-type','text/html')
                    self.end_headers()
                    message =''
                    message += "<html><body>"
                    message += "<h1>Are you sure you want to delete %s ?</h1>" %restaurantQuery.name
                    message += "<form method =post enctype = 'multipart/form-data action '/restaurants/%s/delete'> "
                    message += "<input type = 'submit' value ='Delete'>"
                    message += "</form></body></html>"
                    self.wfile.write(message)
                    return

        except IOError:
            self.send_error("404 File not found: %s" % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # Create new Restaurant Object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('updatedName')

                    restaurantIdPath = self.path.split("/")[2]
                    restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIdPath).one()

                    # Create new Restaurant Object
                    if(restaurantQuery!=[] ):
                        restaurantQuery.name = messagecontent[0]
                        session.add(restaurantQuery)
                        session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                restaurantIdPath = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIdPath).one()

                # Create new Restaurant Object
                if(restaurantQuery != [] ):
                    session.delete(restaurantQuery)
                    session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), WebServerHandler)
        print "webserver is running"
        server.serve_forever()
    except KeyboardInterrupt:
        print "^c pressed ,stopping server"
        server.socket.close()

if __name__ == '__main__':
    main()