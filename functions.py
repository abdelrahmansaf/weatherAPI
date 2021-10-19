import datetime
from flask import  jsonify


def datafilter(dataWeather):
    dicto={}
    cityWeather = dataWeather['consolidated_weather']
    keys_to_remove = ['min_temp', 'wind_direction', 'air_pressure', 'visibility', 'predictability',
                'humidity', 'wind_speed', 'id', 'created', 'wind_direction_compass', 'weather_state_abbr', 'max_temp']

    for key in keys_to_remove:
        for i in range(len(cityWeather)):
            cityWeather[i]['the_temp'] =int(cityWeather[i]['the_temp'])
            cityWeather[i]['the_temp'] =str(cityWeather[i]['the_temp'])
            
            del cityWeather[i][key]

            if (cityWeather[i]['weather_state_name'] == "Showers" or
            cityWeather[i]['weather_state_name'] == "Heavy Rain" or 
            cityWeather[i]['weather_state_name'] == "Light Rain" or 
            cityWeather[i]['weather_state_name'] == "Heavy Cloud") :

                link = "https://random.dog/woof.json"

            elif (cityWeather[i]['weather_state_name'] == "Sunny" or
            cityWeather[i]['weather_state_name'] ==  "Light Cloud" or 
            cityWeather[i]['weather_state_name'] == "Clear"
            ):
                link = "https://aws.random.cat/meow"

            else :
                link = "https://shibe.online/"
            
            cityWeather[i]['picture_weather'] = link
    for i in range(len(cityWeather)) :
        cityWeather[i]['applicable_date'] 
        v = cityWeather[i]['applicable_date']
        v = datetime.datetime.strptime(v, '%Y-%m-%d')
        v = ('{0}-{1}-{2:02}'.format(v.month, v.day, v.year))

        v2 = cityWeather[i]['weather_state_name']
        v3 = cityWeather[i]['the_temp']
    
        del cityWeather[i]['applicable_date']
        del cityWeather[i]['weather_state_name']
        del cityWeather[i]['the_temp']
        cityWeather[i]['Day'] = v
        cityWeather[i]['weather'] = v2
        cityWeather[i]['temperature'] = v3

    dicto["content"] = cityWeather
    return jsonify(dicto)

