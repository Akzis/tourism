from peewee import *

db = SqliteDatabase('places.db')

class BaseModel(Model):
    class Meta:
        database = db

class Place(BaseModel):
    name = CharField()
    address = TextField()
    lon = FloatField()
    lat = FloatField()



from flask import Flask, render_template
from models import db, Place
import requests

app = Flask(__name__)
db.connect()
db.create_tables([Place])


YANDEX_API_KEY = "a24491d9-0cde-46d5-aa70-07ed380b2649"


def fetch_places():
    url = 'https://search-maps.yandex.ru/v1/'
    params = {
        'apikey': YANDEX_API_KEY,
        'text': 'достопримечательность',
        'lang': 'ru_RU',
        'type': 'biz',
        'll': '37.620070,55.753630',  # Москва, пример
        'spn': '0.3,0.3',
        'results': 20
    }
    r = requests.get(url, params=params)
    data = r.json()

    for feature in data.get('features', []):
        props = feature['properties']['CompanyMetaData']
        name = props.get('name')
        address = props.get('address')
        lon, lat = feature['geometry']['coordinates']

        if not Place.select().where(Place.name == name).exists():
            Place.create(name=name, address=address, lon=lon, lat=lat)

@app.route('/')
def index():
    fetch_places()  # Комментируй после первого вызова
    places = Place.select()
    return render_template('map.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)
