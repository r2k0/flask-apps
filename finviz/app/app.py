from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "finviz app"


@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        value_one = int(request.form['number-one'])
        value_two = int(request.form['number-two'])
        total = value_one + value_two
        data = {"total": str(total)}
        return jsonify(data)
    return render_template('index.html',string="TESTING!")

if __name__ == '__main__':
    app.run(debug=True)
