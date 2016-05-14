from Cuterest import *

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=False, nullable=False)


	def __init__(self, name):
		self.name = name

