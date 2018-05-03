from flask import Flask, redirect, url_for, render_template, request
from flask import render_template, url_for, redirect, request, abort
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
		

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='XLS example', template_mode='bootstrap3')


from app import routes, models, modelviews