from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Moment Analysis"


@app.route("/welcome")
def welcome():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    load = request.form["load"]
    type = request.form["type"]
    print(type)
    length = request.form["length"]
    # call method to calc moment
    result = cal_moment(load, length)
    return render_template("result.html", result=result)


@app.route("/form")
def form():
    return render_template("form.html")


def cal_moment(load, length):
    """calc moment for cantilever with point load at end"""
    formula = int(length) * int(load)
    return formula


if __name__ == "__main__":
    app.run(debug=True)


# cantilever beam
# load size
# load type
# length of beam
# formula

# load >>> float
# type>>> drop down >> point load and udl
# length of beam >>> float
