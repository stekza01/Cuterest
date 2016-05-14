from Cuterest import *

@app.route('/')
def hello():
	items = db.session.query(Item)
	return render_template('hello.html', mylist=items)

