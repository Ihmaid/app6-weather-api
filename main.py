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
    # Generates the filename concatenating the filled station number with the
    # archives path to extract the chosen station
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"

    # Generates the dataframe
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    # Locates the item in DATE column which is equal to the introduced date
    # and returns the referent item from TG column
    # The squeeze method transforms an pandas series into a scalar item
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# The app only is executed when the main.py file is executed
if __name__ == "__main__":
    # The specified port allow that other apps run at the default port 5000
    app.run(debug=True, port=5001)
