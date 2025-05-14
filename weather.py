
from flask import Flask, request, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

#

def fetch_weather_data(lat, lon):
     api_key = '39aaddf481b00e72a5ecd353813dd880'
     url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
     response = requests.get(url)
     data = response.json()

     weather_data = {
             'temperature': data['main']['temp'],
             'humidity': data['main']['humidity'],
             'wind_speed': data['wind']['speed'],
             'pressure': data['main']['pressure'],
             'real_feel': data['main']['feels_like'],
             'clouds': data['clouds']['all'],
     }         
     return weather_data


@app.route('/weather', methods=['GET'])
def get_weather():
     lat = request.args.get('lat')
     lon = request.args.get('lon')
     if not lat or not lon:
          return jsonify({"error": "Latitude and longitude required"}), 400
    
    # Получаем данные о погоде
    
     weather_data = fetch_weather_data(lat, lon)
    
    
     print(weather_data)
    
    # Передаем данные в шаблон HTML
     return render_template('test.html', weather=weather_data)



if __name__ == '__main__':

    app.run(debug=True)


