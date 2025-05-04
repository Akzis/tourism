from flask import Blueprint, render_template, request, redirect, session
from models import Place, PlaceImage, Country, Region, RegionPlace, RegionPlaceImage
import peewee
import requests

from wether import fetch_weather_data

places_blueprint = Blueprint('places_blueprint', __name__, url_prefix=None)

def get_places_count():
    return Place.select().count()


@places_blueprint.app_context_processor
def inject_get_places_count():
    return { 'get_places_count': get_places_count }



@places_blueprint.route('/') 
def index(): 
    countries = Country.select()
    
    all_place_images = PlaceImage.select()

    return render_template('index.html', countries=countries, all_place_images=all_place_images) 



@places_blueprint.route('/country/<int:country_id>/')
def country(country_id):
    country = Country.get_by_id(country_id)

    places = Place.select(
        Place.name,
        Place.description,
        Place.id,
        peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
        Place.country_id
    ).join(PlaceImage).objects().group_by(Place).where(Place.country_id==country_id)

    for place in places:
        place.url = place.url.split(",")

    # places = Place.select(
    #     Place.name,
    #     Place.description,
    #     Place.id,
    #     Place.country_id
    # ).join(PlaceImage).where(Place.country_id == country_id)
        
    return render_template('country.html', country = country, places = places)





#39aaddf481b00e72a5ecd353813dd880

@places_blueprint.route('/add_to_visit/<int:place_id>/', methods=['POST'])
def add_to_visit(place_id):
    if ('visited_places_id' not in session):
        session['visited_places_id'] = []

    session['visited_places_id'] = [*session['visited_places_id'], place_id]
    
    print(session['visited_places_id'])

    return redirect('/countrysearch/')



# @places_blueprint.route('/add_to_visit_russia/<int:regionplace_id>/', methods=['POST'])
# def add_to_visit_russia(regionplace_id):
#     if ('visited_places_id_russia' not in session):
#         session['visited_places_id_russia'] = []

#     session['visited_places_id_russia'] = [*session['visited_places_id_russia'], regionplace_id]
    
#     print(session['visited_places_id_russia'])

#     return redirect('/countrysearchplace/russia/')





@places_blueprint.route('/place/<int:place_id>/', methods=['POST', 'GET'])
def place(place_id):
    images = PlaceImage.select().where(PlaceImage.place_id == place_id)

    # place = Country.get_by_id(place_id)
    # places = Place.select(
    #     Place.name,
    #     Place.description,
    #     Place.id,
    #     peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
    #     Place.country_id
    # ).join(PlaceImage).objects().group_by(Place).where(Place.place==place)

    # for place in places:
    #     place.url = place.url.split(",")
    
    
    # if 'user_id' not in session:
    #     return redirect(url_for('login'))  # Перенаправление на страницу логина

    place = Place.get(Place.id == place_id)
    try:
        data = fetch_weather_data(place.latitude, place.longitude)
    except:
        data = None

    is_liked = False

#     if ('user_id' in session and User.select()):
#         user = User.get(User.id == session['user_id'])
#         is_liked = Like.select().where((Like.place_id == place.id) and (Like.user_id == user.id)).exists()

#         if (request.method == 'POST'):
#             # Проверяем, не лайкал ли пользователь это место ранее
#             if not Like.select().where((Like.user_id == user.id) & (Like.place_id == place.id)).exists():
#                 # pass
#                 Like.create(user_id=user.id, place_id=place.id)

#     likes = Like.select().where(Like.place_id == place_id).count()

#     print(likes, place_id)

    return render_template(
         'place.html',
         place = place,
         images = images,
         is_liked=is_liked,
         data=data,

     #     likes_count=likes
     )
    




@places_blueprint.route('/regionplace/<int:regionplace_id>/', methods=['POST', 'GET'])
def regionplace(regionplace_id):
    images = RegionPlaceImage.select().where(RegionPlaceImage.regionplace_id == regionplace_id)


    regionplace = RegionPlace.get(RegionPlace.id == regionplace_id)
    try:
        data = fetch_weather_data(regionplace.latitude, regionplace.longitude)
    except:
        data = None
    print(data)

    is_liked = False

    return render_template(
         'regionplace.html',
         regionplace = regionplace,
         images = images,
         is_liked=is_liked,
         data=data,

     )