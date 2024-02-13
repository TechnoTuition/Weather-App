import json

import requests
from flask import Flask, render_template, request, redirect,jsonify

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


@app.route("/docs")
def api_docs():
    return render_template("Apidocs.html")


User_api_url = f"https://surajprajapati.pythonanywhere.com/api"
@app.get("/api")
def api_request():

    city = request.args.get('cityname')
    URL = f' https://api.weatherapi.com/v1/current.json?key={API_key}={city}'
    r = requests.get(URL)

    data = r.json()
    print(r.json())
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(port=3000, debug=True, host="0.0.0.0")
