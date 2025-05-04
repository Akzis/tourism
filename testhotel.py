from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'YOUR_API_KEY'

@app.route('/')
def index():
    latitude = 'YOUR_LATITUDE'
    longitude = 'YOUR_LONGITUDE'
    radius = '20'  # расстояние в километрах от координат

    url = f'https://engine.hotellook.com/api/v2/lookup.json?query=54.699771,20.505330&lang=ru&lookFor=both&limit=10'
    response = requests.get(url)
    hotels = response.json()

    # hotelsearch = {
    #         'name': hotels['main']['name'],
    #         'locationId': hotels['main']['locationId'],}

    hotels = [{
        "location": hotel['location'],
        "name": hotel['name'],
        "id": hotel['id']
        } for hotel in hotels['results']['hotels']]
    print(len(hotels))

    hotels_dict = {}
    
    for hotel in hotels:
        hotels_dict[hotel['name']] = hotel
        # if (hotel['name'] in hotels_dict):
            # hotels_dict[hotel['name']] = hotel

    hotels = [hotels_dict[hotel_name] for hotel_name in hotels_dict]
    
    print(len(hotels))

    return render_template('hotels.html', hotels=hotels)

if __name__ == '__main__':
    app.run(debug=True)
