import os, sys, time
from flask import *
from jinja2 import Template
from flask.ext.sqlalchemy import SQLAlchemy

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

heroku = Heroku(app)
db = SQLAlchemy(app)

# FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



# DATABASE SELECTION
def set_database():
	'''
	Uses a temporary database if the program detects that
	it is running on a mac, otherwise it uses the production
	database on Heroku postgres.
	'''
	if sys.platform == 'darwin':
		# running on a mac
		DATABASE_URL = "sqlite:////tmp/tempdb_rr.db"
	else:
		# heroku postgresql database
		DATABASE_URL = "postgres://cypesbhdqdjwdm:_Fc_oDYnfvYp8Ma5F3aOnJMHXd@ec2-54-83-17-9.compute-1.amazonaws.com:5432/d5r02un6qtqh6h"


	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

set_database()


#DatabaseTables
#add the imports for those here




#modules
#add admin files imports here

import Cuterest.admin.helloheroku
