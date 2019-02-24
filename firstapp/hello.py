import webapp2



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" name="my_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        username = (self.request.get("my_name"))
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)

import webapp2


def convert_temp(cel_temp):
    ''' convert Celsius temperature to Fahrenheit temperature '''
    if cel_temp == "":
        return ""
    try:
        far_temp = float(cel_temp) * 9 / 5 + 32
        far_temp = round(far_temp, 3)  # round to three decimal places
        return str(far_temp)
    except ValueError:  # user entered non-numeric temperature
        return "invalid input"


class MainPage(webapp2.RequestHandler):
    def get(self):
        cel_temp = self.request.get("cel_temp")
        far_temp = convert_temp(cel_temp)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Temperature Converter</title></head>
            <body>
              <form action="/" method="get">
                Celsius temperature: <input type="text"
                                        name="cel_temp" value={}>
                <input type="submit" value="Convert"><br>
                Fahrenheit temperature: {}
              </form>
            </body>
          </html>""".format(cel_temp, far_temp))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
