from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('template.html',my_string="Jinja exercise:",\
            my_list=[0,1,2,3,4,5,6,7,8],title="Home")

@app.route("/about")
def about():
    return render_template('template.html',my_string="Jinja exercise:",\
            my_list=[0,1,2,3,4,5,6,7,8],title="About")

@app.route("/contact")
def contact():
    return render_template('template.html',my_string="Jinja exercise:",\
            my_list=[0,1,2,3,4,5,6,7,8],title="Contact Us")


if __name__ == '__main__':
    app.run(debug=True)
