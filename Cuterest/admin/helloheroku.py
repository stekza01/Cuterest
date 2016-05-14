from Cuterest import *

@app.route('/')
def hello():
	return render_template('hello.html')

