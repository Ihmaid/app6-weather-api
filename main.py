from flask import Flask, render_template

app = Flask(__name__)


# The @ is a decorator, and when the browser receive the url extension which is
# in parentheses it will call and execute the function
@app.route("/")
def home():
    return render_template("home.html")


# The names are into <> to demonstrate to flask that the user can insert
# another value into the url
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}

# The app only is executed when the main.py file is executed
if __name__ == "__main__":
    app.run(debug=True)
