from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
	return render_template('hello.html')


#these are optional for Heroku deploy
if __name__ == "__main__":
	app.run()
