import json

import requests
from flask import Flask, render_template, request, redirect

API_key = "c56326a851cc41eba5e170519230504&q"

#


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index(cityName=None):
    cityName = request.form.get("city")

    if (cityName):

        return redirect(f"/{cityName}")
    else:
        return render_template('index.html')

    return render_template("index.html")


@app.route("/<cityName>")
def get_detail(cityName):
    print(cityName)
    URL = f' https://api.weatherapi.com/v1/current.json?key={API_key}={cityName}'
    r = requests.get(URL)

    data = r.json()
    print(r.json())

    return render_template("showdetail.html", data=data)


if __name__ == '__main__':
    app.run(port=3000, debug=True, host="0.0.0.0")
