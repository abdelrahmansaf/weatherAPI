import requests
from flask import Flask, request
from flask import  jsonify
from functions import  datafilter

app = Flask(__name__)


@app.route('/api/weather/')
def hello():
    return "Welcome mate !!"


@app.route('/api/weather/<city>', methods=['POST'])
def citySearch2(city):
    payload = {"query": city}
    code = requests.get("https://www.metaweather.com/api/location/search/",params=payload)

    if code.status_code == 200 and len(code.json())== 1:

        payload2 = {'picture': request.json['picture']}

        if payload2["picture"] == "dog" :
            picture = "https://random.dog/woof.json"

        elif payload2["picture"] == "cat":
            picture = "https://aws.random.cat/meow"

        elif payload2["picture"] == "fox" :
            picture = "https://shibe.online/"
        
        else :
            picture = "ERROR! Not Valid Picture"

        payload = {'picture':picture}

        return jsonify(payload)

    else :
        valueFalse = {
        "content": [],
        "error": {
        "msg":"Town not found",
        "uid_error": "4"
            }
            }
        return jsonify(valueFalse)


    
@app.route('/api/weather/<city>', methods=['GET'])
def citySearch(city):
    payload = {"query": city}
    data = requests.get("https://www.metaweather.com/api/location/search/",params=payload).json()
    if len(data) == 1:
        codeWoeid = []
        for item in data:
            codeWoeid.append(item['woeid'])
        id = str(codeWoeid[0])
        api = f'https://www.metaweather.com/api/location/{id}'
        dataWeather = requests.get(api).json()
        return datafilter(dataWeather)

    elif len(data) == 0 :
        valueFalse = {
        "content": [],
        "error": {
        "msg":"Town not found",
        "uid_error": "4"
            }
            }
        return jsonify(valueFalse)

    elif len(data)  > 2 :
        return jsonify(data)

    

if __name__ == '__main__':
    app.run(debug=True)

