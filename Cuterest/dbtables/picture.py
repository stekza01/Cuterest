from Cuterest import *

class Picture(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), unique=False)
	description = db.Column(db.String(200), unique=False)
	url = db.Column(db.String(200), unique=False, nullable=False)
	boardid = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, boardid, name, description, url):
		self.boardid = boardid
		self.name = name
		self.description = description
		self.url = url


