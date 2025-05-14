from flask import Flask, render_template, redirect, flash, Response
import peewee
from peewee import *
from flask_peewee.db import SqliteDatabase
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.peewee import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session
from models import *
from places import places_blueprint
from users import users_blueprint
from request import request_blueprint
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException

"https://gjaw:jgkawgaw@127.0.0.1"
# http://127.0.0.1:5000/

#pip freeze > requirements.txt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dragon'
app.config['BASIC_AUTH_USERNAME'] = 'user2'
app.config['BASIC_AUTH_PASSWORD'] = '123'
app.config['BASIC_AUTH_REALM'] = '/admin/'

# @app.route('/profil')
# def profil():
#     if 'user_id' in session:
#         user = User.get(User.id == session['user_id'])
#         return render_template('profil.html', user=user)
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         try:
#             user = User.get(User.username == username)
#             if user.check_password(password):
#                 session['user_id'] = user.id
#                 return redirect(url_for('profil'))
#         except User.DoesNotExist:
#             pass
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if not User.select().where(User.username == username).exists():
#             user = User(username=username)
#             user.set_password(password)  # Установка пароля перед сохранением
#             user.save()
#             session['user_id'] = user.id
#             return redirect(url_for('profil'))
#     return render_template('register.html')

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     return redirect(url_for('login'))



# @app.route('/click', methods=['POST'])
# def click():
#     if 'user_id' in session:
#         user = User.get(User.id == session['user_id'])
#         Like.likes += 1
#         Like.save()
#         return str(Like.likes)
#     return '0'





# def get_places_count():
#     return Place.select().count()

# @app.context_processor
# def inject_get_places_count():
#     return { 'get_places_count': get_places_count }



# @app.route('/success')
# def success():
#     return render_template('success.html')

# # Путь для создания заявки
# @app.route('/request/', methods=['GET', 'POST'])
# def create_request():
#     form = RequestForm()
#     if form.validate_on_submit():
#         Request.create(
#             name=form.name.data,
#             email=form.email.data,
#             subject=form.subject.data,
#             message=form.message.data,
#         )
#         return redirect('/success')
#     return render_template('request.html', form=form)

# @app.route('/') 
# def index(): 
#     countries = Country.select()
    
#     all_place_images = PlaceImage.select()

#     return render_template('index.html', countries=countries, all_place_images=all_place_images) 


# @app.route('/country/<int:country_id>/')
# def country(country_id):
#     country = Country.get_by_id(country_id)
#     places = Place.select(
#         Place.name,
#         Place.description,
#         Place.id,
#         peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
#         Place.country_id
#     ).join(PlaceImage).objects().group_by(Place).where(Place.country_id==country_id)

#     for place in places:
#         place.url = place.url.split(",")

#     # places = Place.select(
#     #     Place.name,
#     #     Place.description,
#     #     Place.id,
#     #     Place.country_id
#     # ).join(PlaceImage).where(Place.country_id == country_id)
        
#     return render_template('country.html', country = country, places = places)

# @app.route('/place/<int:place_id>/', methods=['POST', 'GET'])
# def place(place_id):
#     images = PlaceImage.select().where(PlaceImage.place_id == place_id)

#     # place = Country.get_by_id(place_id)
#     # places = Place.select(
#     #     Place.name,
#     #     Place.description,
#     #     Place.id,
#     #     peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
#     #     Place.country_id
#     # ).join(PlaceImage).objects().group_by(Place).where(Place.place==place)

#     # for place in places:
#     #     place.url = place.url.split(",")
    
    
#     # if 'user_id' not in session:
#     #     return redirect(url_for('login'))  # Перенаправление на страницу логина

#     place = Place.get(Place.id == place_id)

#     is_liked = False
    
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









    
#     return render_template('place.html', place = place, images = images, likes_count=likes, is_liked=is_liked)
    
app.register_blueprint(places_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(request_blueprint)

basic_auth = BasicAuth(app)


# class DashboardView(AdminIndexView): 
	
# 	@expose('/') 
# 	def admin_custom(self): 
# 	   return self.render('dashboard_index.html')



class AuthException(HTTPException):
    def __init__(self, message):
        # python 2
        # super(AuthException, self).__init__(message, Response(
        #     message, 401,
        #     {'WWW-Authenticate': 'Basic realm="Login Required"'}
        # ))
        # # python 3
        super().__init__(message, Response(
            message, 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class BaseModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated. Refresh the page.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


class RequestAdminView(BaseModelView):
    column_list = ('name', 'email', 'subject', 'message')
    form_widget_args = {
        'email':{
            'readonly': True
        },
        'name': {
            'readonly': True
        },
        'subject':{
            'readonly': True
        },
        'message':{
            'readonly': True
        },
    }


 

@app.route('/countrysearch/')
def countrysearch():
    countries = Country.select()
    places = Place.select(
        Place.name,
        Place.latitude,
        Place.longitude,
        Place.id)
    
    visited_places = []
    route_url = None

    if 'visited_places_id' in session:
        visited_places = Place.select().where(Place.id << session['visited_places_id'])
        coords = [(places.latitude, places.longitude) for places in visited_places]
        if coords:
            route_points = "~".join([f"{lat},{lon}" for lat, lon in coords])
            route_url = f"https://yandex.ru/maps/?rtext={route_points}&rtt=auto"



    return render_template('searchcountry.html', countries=countries, places = places, visited_places=visited_places, route_url=route_url)


# @app.route('/logout_admin/', methods=["POST"])
# def logout_admin():
#     print("gkawgwa")
#     return redirect("http://log:out@127.0.0.1:5000")

@app.route('/countrysearchplace/<int:countrysearch_id>/')
def countrysearchplace(countrysearch_id):
    countries = Country.select()
    country = Country.get_by_id(countrysearch_id)
    places = Place.select(
        Place.name,
        Place.id,
        Place.latitude,
        Place.longitude,
        peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
        Place.country_id
    ).join(PlaceImage).objects().group_by(Place).where(Place.country_id==countrysearch_id)


    for place in places:
        place.url = place.url.split(",")


    if ('visited_places_id' in session):
        visited_places = Place.select().where(Place.id << session['visited_places_id'])
    else:
        visited_places = []

    return render_template('countrysearchplace.html', countries=countries, places = places, visited_places=visited_places)


@app.route('/countrysearchplace/russia/')
def countrysearchplace_russia():
    countries = Country.select()
    regions = Region.select()
    regionplaces = RegionPlace.select(
        RegionPlace.name,
        RegionPlace.description,
        RegionPlace.id,
        peewee.fn.GROUP_CONCAT(RegionPlaceImage.url).alias('url'),
        RegionPlace.region_id
    )




    visited_places = []
    route_url = None

    if 'visited_places_id' in session:
        visited_places = RegionPlace.select().where(RegionPlace.id << session['visited_places_id'])
        coords = [(regionplaces.latitude, regionplaces.longitude) for regionplaces in visited_places]
        if coords:
            route_points = "~".join([f"{lat},{lon}" for lat, lon in coords])
            route_url = f"https://yandex.ru/maps/?rtext={route_points}&rtt=auto"

    return render_template(
        'countrysearchplace_russia.html',
        countries=countries,
        regionplaces=regionplaces,
        visited_places=visited_places,
        regions=regions,

    )



@app.route('/countrysearchplace/russia/<int:countrysearch_id>/')
def countrysearch_place_region(countrysearch_id):
    countries = Country.select()
    regions = Region.select()
    region = Region.get_by_id(countrysearch_id)
    # regionplaces = RegionPlace.select(
    #     RegionPlace.name,
    #     RegionPlace.latitude,
    #     RegionPlace.longitude,
    #     RegionPlace.id,).where(RegionPlace.region_id == countrysearch_id)
    




    regionplaces = RegionPlace.select(
        RegionPlace.name,
        RegionPlace.description,
        RegionPlace.id,
        peewee.fn.GROUP_CONCAT(RegionPlaceImage.url).alias('url'),
        RegionPlace.region_id
    ).join(RegionPlaceImage).objects().group_by(RegionPlace).where(RegionPlace.region_id==countrysearch_id)

    for regionplace in regionplaces:
        if (regionplace.url):
            regionplace.url = regionplace.url.split(",")



    if ('visited_places_id' in session):
        visited_places = RegionPlace.select().where(RegionPlace.id << session['visited_places_id'])
    else:
        visited_places = []

        
    ## доделать
    # visited_places = []
    # route_url = None

    # if 'visited_places_id' in session:
    #     visited_places = RegionPlace.select().where(RegionPlace.id << session['visited_places_id'])
    #     coords = [(regionplaces.latitude, regionplaces.longitude) for regionplaces in visited_places]
    #     if coords:
    #         route_points = "~".join([f"{lat},{lon}" for lat, lon in coords])
    #         route_url = f"https://yandex.ru/maps/?rtext={route_points}&rtt=auto"



    return render_template('countrysearchplace_region.html', countries=countries, regionplaces = regionplaces, visited_places=visited_places,regions = regions)




# @app.route('/countrysearchplace/russia/')
# def countrysearchplace_russia():
#     countries = Country.select()
#     regions = Region.select()

#     regionplaces = RegionPlace.select(
#         RegionPlace.name,
#         RegionPlace.id,
#         RegionPlace.latitude,
#         RegionPlace.longitude,)
        
#     if ('visited_places_id_russia' in session):
#         visited_places_russia = RegionPlace.select().where(RegionPlace.id << session['visited_places_id_russia'])
#     else:
#         visited_places_russia = []

#     return render_template('countrysearchplace_russia.html', countries=countries, regionplaces = regionplaces, visited_places_russia=visited_places_russia, regions = regions)


# @app.route('/countrysearchplace/russia/<int:countrysearch_id>/')
# def countrysearch_place_region(countrysearch_id):
#     countries = Country.select()
#     regions = Region.select()
#     region = Region.get_by_id(countrysearch_id)
#     regionplaces = RegionPlace.select(
#         RegionPlace.name,
#         RegionPlace.latitude,
#         RegionPlace.longitude,
#         RegionPlace.id,).where(RegionPlace.region_id == countrysearch_id)
    
#     if ('visited_places_id_russia' in session):
#         visited_places_russia = RegionPlace.select().where(RegionPlace.id << session['visited_places_id_russia'])
#     else:
#         visited_places_russia = []

#     return render_template('countrysearchplace_region.html', countries=countries, regionplaces = regionplaces, visited_places_russia=visited_places_russia,regions = regions)





@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect(url_for('countrysearch'))


@app.route('/russia/')
def russia():
    region = Region.select()
    # places = Region.select(
    #     Region.name,
    #     Region.description,
    #     Region.id,
        # peewee.fn.GROUP_CONCAT(PlaceImage.url).alias('url'),
    # ).join(PlaceImage).objects().group_by(Place)
    # for place in places:
    #     place.url = place.url.split(",")
    return render_template('russia.html', regions = region)


@app.route('/region/<int:region_id>/')
def region(region_id):
    region = Region.get_by_id(region_id)
    city = request.args.get('city') 
    cities = (RegionPlace
            .select(RegionPlace.city)
            .where(RegionPlace.region_id == region_id)
            .distinct())

    regionplaces = RegionPlace.select(
        RegionPlace.name,
        RegionPlace.description,
        RegionPlace.id,
        peewee.fn.GROUP_CONCAT(RegionPlaceImage.url).alias('url'),
        RegionPlace.region_id
    ).join(RegionPlaceImage, peewee.JOIN.LEFT_OUTER).objects().group_by(RegionPlace).where(RegionPlace.region_id==region_id)


    if city:
        regionplaces = regionplaces.where(RegionPlace.city == city)

    for regionplace in regionplaces:
        if (regionplace.url):
            regionplace.url = regionplace.url.split(",")

        
    return render_template('region.html', region = region, regionplaces = regionplaces, cities=cities, selected_city=city)







if (__name__ == "__main__"):   
    try:
        db.create_tables([Country, Place, PlaceImage, Request, Like, User, Region, RegionPlace, RegionPlaceImage, LikeRussia])
    except:
        pass
    
    admin = Admin(app)
    # admin = Admin(app)

    admin.add_view(BaseModelView(Country))
    # admin.add_view(ModelView(CountryImage))
    admin.add_view(BaseModelView(Place))
    admin.add_view(BaseModelView(PlaceImage))
    admin.add_view(RequestAdminView(Request))
    admin.add_view(BaseModelView(Like))
    admin.add_view(BaseModelView(User))
    admin.add_view(BaseModelView(Region))
    admin.add_view(BaseModelView(RegionPlace))
    admin.add_view(BaseModelView(RegionPlaceImage))
    admin.add_view(BaseModelView(LikeRussia))
    app.run(debug=True)






#58.446174	14.884029	Вадстенский замок	Начать знакомство стоит с впечатляющего напоминания о славной истории государства. На его территории описываемая крепость является одной из самых старинных, ведь строить ее начали еще в 1545 году. Далеко не всем туристам известно, что изначально Вадстенский замок имел 4 круглых башни, 3 жилых здания из камня, несколько хозяйственных построек. В определенный момент необходимость в фортификационных сооружениях отпала, поэтому они были скрыты. Решение превратить постройку в исторический памятник было принято в XX веке, для чего были проведены масштабные реставрационные работы.	1