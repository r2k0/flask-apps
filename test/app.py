from flask import Flask

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

def test():
	return "testing Flask!"

if __name__ == "__main__":
	app.run()
