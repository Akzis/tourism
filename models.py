from flask import Flask, render_template, redirect, flash
import peewee
from peewee import *
from flask_peewee.db import SqliteDatabase
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session
import requests
# Инициализация базы данных

db = SqliteDatabase('database.db')

# Определение модели данных
class Country(db.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    description = peewee.CharField()
    image = peewee.CharField()
    side_of_the_world = peewee.CharField(
        choices=[
            ("Asia", "Азия"),
            ("Europe", "Европа"),
            ("South America", "Южная америка"),
            ("North America", "Северная америка"),
            ("Australia and Oceania", "Австралия и Океания"),
            ("Africa", "Африка")
        ],
    )



# class Changeside_of_the_world(FlaskForm):
#     side_of_the_world = StringField(
#         "Новый статус",
#         choices=[
#             ("Asia", "Азия"),
#             ("Europe", "Европа"),
#             ("America", "Америка"),
#             ("Australia and Oceania", "Австралия и Океания"),
#             ("Africa", "Африка")
#         ],
#         validators=[]
#     )


# class CountryImage(db.Model):
#     id = peewee.PrimaryKeyField()
#     url = peewee.CharField()
#     country_id = peewee.ForeignKeyField(Country)

class Place(db.Model):
    id = peewee.PrimaryKeyField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    name = peewee.CharField()
    description = peewee.CharField()
    country_id = peewee.ForeignKeyField(Country)

class PlaceImage(db.Model):
    id = peewee.PrimaryKeyField()
    url = peewee.CharField()
    place_id = peewee.ForeignKeyField(Place)


class Region(db.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    description = peewee.CharField()
    image = peewee.CharField()

class RegionPlace(db.Model):
    id = peewee.PrimaryKeyField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    name = peewee.CharField()
    description = peewee.CharField()
    region_id = peewee.ForeignKeyField(Region)

class RegionPlaceImage(db.Model):
    id = peewee.PrimaryKeyField()
    url = peewee.CharField()
    regionplace_id = peewee.ForeignKeyField(RegionPlace)





class Request(db.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    email = peewee.CharField()
    subject = peewee.CharField()
    message = peewee.CharField()



class User(db.Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

    def set_password(self, password):
        # self.password = generate_password_hash(password)
        self.password = (password)

    def check_password(self, password):
        # return check_password_hash(self.password, password)
        return (self.password, password)


class Like(db.Model):
    id = peewee.PrimaryKeyField()
    user_id = peewee.ForeignKeyField(User)
    place_id = peewee.ForeignKeyField(Place)
    likes = IntegerField(default=0)

    
    
    
    
    

class RequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])

    submit = SubmitField('Submit')