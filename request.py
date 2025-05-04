from flask import Blueprint, render_template
from models import *
import peewee


request_blueprint = Blueprint('request_blueprint', __name__)



@request_blueprint.route('/success')
def success():
    return render_template('success.html')

# Путь для создания заявки
@request_blueprint.route('/request/', methods=['GET', 'POST'])
def create_request():
    form = RequestForm()
    if form.validate_on_submit():
        Request.create(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data,
        )
        return redirect('/success')
    return render_template('request.html', form=form)
