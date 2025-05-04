from flask import Blueprint, render_template
from models import *
import peewee


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/profil')
def profil():
    if 'user_id' in session:
        user = User.get(User.id == session['user_id'])
        
        liked_places = Like.select().where(Like.user_id == user.id, Like.likes == 1)

        for place in liked_places:
            print(place)
        
        return render_template('profil.html', user=user)
    return redirect(url_for('users_blueprint.login'))



@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.get(User.username == username)
            if user.check_password(password):
                session['user_id'] = user.id
                return redirect(url_for('users_blueprint.profil'))
        except User.DoesNotExist:
            pass
    return render_template('login.html')

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not User.select().where(User.username == username).exists():
            user = User(username=username)
            user.set_password(password)  # Установка пароля перед сохранением
            user.save()
            session['user_id'] = user.id
            return redirect(url_for('users_blueprint.profil'))
    return render_template('register.html')

@users_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    # raise AuthException('Successfully logged out.')
    return redirect(url_for('users_blueprint.login'))

def get_place_likes_count(place_id):
    return Like.select().where(Like.place_id==place_id).count()

@users_blueprint.app_context_processor
def inject_place_likes_count():
    return { 'get_place_likes_count': get_place_likes_count }

@users_blueprint.route('/like/')
def like():
    return {}

@users_blueprint.route('/like/<int:place_id>/', methods=['POST'])
def toggle_like(place_id):
    user_id = session['user_id']

    is_liked = Like.select().where(Like.user_id==user_id, Like.place_id==place_id).exists()
   
    if (is_liked):
        Like.get(Like.user_id == user_id, Like.place_id == place_id).delete_instance()
        # Like.select(Like.user_id==user_id, place_id == place_id).delete_instance()
    else:
        Like.create(place_id=place_id, user_id = user_id)
    
    return redirect(f'/place/{place_id}/')