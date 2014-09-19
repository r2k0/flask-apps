from flask import Flask
""" learning and experimenting with Flask """

# create an instance of the Flask class and assigned
# it to the varialbe 'app'
app = Flask(__name__)

# decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# dynamic routes
@app.route("/test")
@app.route("/test/<query>")
def search(query):
	return query

#Flask converters
# * <value> is treated as unicode
# * <int:value> is treated as an integer
# * <float:value> is treated as a floating point
# * <path/of/some/sort> is treated as a path

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"

# dynamic route that accpets slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

# Response Object - response, status, headers
# if not explicitly define these, Flask will automatically assign 
# a Status Code of 200 and a header where the Content-Type: "text/html"
#

@app.route("/name/<name>")
def index(name):
	return "Hello, {}".format(name), 200

def test():
	return "testing Flask!"

# run() start the development server
if __name__ == "__main__":
	app.run()
