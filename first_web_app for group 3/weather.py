from flask import Flask, render_template, request

app=Flask(__name__)

import requests

end_point="https://api.openweathermap.org/data/2.5/weather"
api_key="6b8d9643cd8df70131fe3ba87f3f0c6f"

params_1={
    "q":"banha",
    "appid":api_key,
    "units":"metric"
}
params_2={
    "q":"mecca",
    "appid":api_key,
    "units":"metric"
}
respons_1=requests.get(end_point,params_1)
data=respons_1.json()
tempbanha=data["main"]["temp"]
@app.route("/")
def home():
    params_1 = {
        "q": "banha",
        "appid": api_key,
        "units": "metric"
    }
    params_2 = {
        "q": "mecca",
        "appid": api_key,
        "units": "metric"
    }
    respons_1 = requests.get(end_point, params_1)
    data = respons_1.json()
    tempbanha = data["main"]["temp"]
    respons_2 = requests.get(end_point, params_2)
    data2= respons_2.json()
    tempmecca = data2["main"]["temp"]
    return render_template("weather.html",tempbanha=int(tempbanha),tempmecca=int(tempmecca))


@app.route("/search",methods=["GET","POST"])
def search():
    if request.method =="POST":
        city_1=request.form.get("city_1")
        city_2=request.form.get("city_2")
        params_1 = {
            "q": city_1,
            "appid": api_key,
            "units": "metric"
        }
        params_2 = {
            "q": city_2,
            "appid": api_key,
            "units": "metric"
        }
        respons_1 = requests.get(end_point, params_1)
        data = respons_1.json()
        tempbanha = data["main"]["temp"]
        respons_2 = requests.get(end_point, params_2)
        data2 = respons_2.json()
        tempmecca = data2["main"]["temp"]
        return render_template("weather.html", tempbanha=int(tempbanha), tempmecca=int(tempmecca),city_1=city_1,city_2=city_2)
@app.route("/cat")
def cat():
    endpoint="https://api.thecatapi.com/v1/images/search"
    params={
        "x-api-key":"live_YEgUkinhatYqJsyGNbM2upVHrvuPP5m1qxduUMCi2Le4EzVbnnWriaXHcb3Xy33a",
        "limit":100
    }
    moaz=requests.get(endpoint,params)
    data=moaz.json()
    print(data)
    all_pics=[]
    for i in data:
        all_pics.append(i["url"])
    print(all_pics)
    return render_template("cats.html",all=all_pics)

if __name__=="__main__":
    app.run(debug=True)