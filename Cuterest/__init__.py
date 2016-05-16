import os, sys, time
from flask import *
from jinja2 import Template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, StringField, SubmitField, validators
from flask import Flask, render_template, flash, request, url_for
from flask.ext.heroku import Heroku
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = '\xa7h\xb7)\xce\xce\x8c\xa9`\xce\xa1\xdb\x9b1;F\x12c\xb2\xe9\xe7\xe8\x92\xe2'
app.debug = True

heroku = Heroku(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



# DATABASE SELECTION
def set_database():


	if sys.platform == 'linux':
		# running on linux
		DATABASE_URL = "sqlite:////tmp/tempdb_rr.db"
	else:
		# heroku postgresql database
		DATABASE_URL = "postgres://jijqzkddnribvr:7IPm5d755KMycpfXPlmpXaDhtu@ec2-54-163-248-14.compute-1.amazonaws.com:5432/ddtnjdnbt3areo"


	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

set_database()


#DatabaseTables
#add the imports for those here

from Cuterest.dbtables.testdb import Item
from Cuterest.dbtables.users import User
from Cuterest.dbtables.board import Board
from Cuterest.dbtables.picture import Picture




#modules
#add admin files imports here

import Cuterest.admin.helloheroku




db.create_all()
db.session.commit()
