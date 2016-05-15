from Cuterest import *
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String(40), unique=False, nullable=False)
	last = db.Column(db.String(40), unique=False)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(160), unique=False)

	def __init__(self, first, last, email, password):
		self.first = first
		self.last = last
		self.email = email
		self.password = self.generate_password(password)


	def get(myid):
		return db.session.query(User).filter_by(id=myid).first()

	def generate_password(self, pw_plaintext):
		# Returns a SHA-1 salted password from the given plaintext password
		return generate_password_hash(pw_plaintext)

	def check_password(self, pw_plaintext):
		# Checks to see if the plaintext password matches the SHA-1 password
		# that's in the database.
		# Returns True/False
		return check_password_hash(self.password, pw_plaintext)

	def is_authenticated(self):
		# Are we logged in?
		# returns True/False
		return True

	def is_active(self):
		# Returns True/False if this user is not inactive
		return True

	def is_inactive(self):
		# Returns True/False if this user is inactive
		return not self.is_active()

	def is_anonymous(self):
		# This user is not anonymous (thus, is logged in)
		return False

	def get_id(self):
		# return this user's id # from the database
		return self.id

