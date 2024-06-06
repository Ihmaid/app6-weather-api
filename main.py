from flask import Flask, render_template
import pandas as pd

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
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# The app only is executed when the main.py file is executed
if __name__ == "__main__":
    # The specified port allow that other apps run at the default port 5000
    app.run(debug=True, port=5001)
