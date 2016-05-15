from Cuterest import *

class Board(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), unique=False, nullable=False)
	description = db.Column(db.String(40), unique=False)
	userid = db.Column(db.Integer, unique=False)

	def __init__(self, userid, name, des):
		self.name = name
		self.description = des
		self.userid = userid


