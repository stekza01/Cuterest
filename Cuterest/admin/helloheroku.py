from Cuterest import *


class form_CreateUser(Form):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password')

class form_SignIn(Form):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password')

class form_NewBoard(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

class form_NewPic(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    url = StringField('Source URL', validators=[DataRequired()])


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = form_CreateUser()
	if request.method == 'POST':
		print("in signup")
		formdata = request.form
		print("in signup2")
		firstname = formdata['firstname']
		lastname = formdata['lastname']
		email = formdata['email']
		password = formdata['password']

		if createUser(firstname, lastname, email, password):
			#user made successfully
			pass
		else:
			#make this return basic when we get there
			pass

	return render_template('newuser.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
def signin():
	form = form_SignIn()
	if request.method == 'POST':
		formdata = request.form
		email = formdata['email']
		password = formdata['password']
		check = db.session.query(User).filter_by(email=email, password=password).first()
		if check:
			login_user(check)
			return redirect(url_for('hello'))

	return render_template('login.html', form=form)




@app.route('/newboard', methods=['GET', 'POST'])
def makeboard():
	form = form_NewBoard()
	if request.method == 'POST':
		print("here")
		formdata = request.form
		name = formdata['name']
		description = formdata['description']
		userid = current_user.id

		if createBoard(userid, name, description):
			pass
		else:
			pass

	return render_template('newboard.html', form=form)


@app.route('/newpicture/<boardid>', methods=['GET', 'POST'])
def makepic(boardid):
	boardid = int(boardid)
	form = form_NewPic()
	if request.method == 'POST':
		formdata = request.form
		name = formdata['name']
		description = formdata['description']
		url = formdata['url']
		

		if createPicture(boardid, name, description, url):
			pass
		else:
			pass

	return redirect(url_for('viewboard', boardid = boardid))


@app.route('/viewboard/<boardid>', methods=['GET', 'POST'])
def viewboard(boardid):
	boardid = int(boardid)
	myboard = db.session.query(Board).filter_by(id=boardid).first()
	myimages = db.session.query(Picture).filter_by(boardid=boardid)
	mylist = []
	for item in myimages:
		mylist.append(item)


	return render_template('images.html', mylist=mylist, boardid=boardid)


@app.route('/profile', methods=['GET', 'POST'])
def viewuserboards():
	userid = current_user.id
	myboards = db.session.query(Board).filter_by(userid=userid)
	boardlist = []
	for item in myboards:
		boardlist.append(item)


	return render_template('boards.html', mylist=boardlist)

@app.route('/ajax', methods = ['POST'])
def ajax_request():
	source = request.form['src']
	name = request.form['name']
	desc = request.form['desc']
	boardid = int(request.form['boardid'])
	if createPicture(boardid, name, desc, source):
		pass
	else:
		pass
	return jsonify(thename=name, thesrc=source, thedesc=desc)


@app.route('/')
def hello():
	items = db.session.query(User)
	items2 = db.session.query(Board)
	items3 = db.session.query(Picture)
	return render_template('hello.html', mylist=items, mylist2=items2, mylist3=items3)




def createUser(fn, ln, em, pw):
    # Adds a user to the database.
    # Returns True if user added successfully, else False.
    try:
        me = User(fn, ln, em, pw)
        db.session.add(me)
        db.session.commit()
        print("User created")
        return True

    except Exception as e:
        # Prints why the user could not be added in the terminal.
        print(e)
        return False


def createBoard(uid, name, des):
    # Adds a user to the database.
    # Returns True if user added successfully, else False.
    try:
        me = Board(uid, name, des)
        db.session.add(me)
        db.session.commit()
        return True

    except Exception as e:
        # Prints why the user could not be added in the terminal.
        print(e)
        return False


def createPicture(bid, name, des, url):
    # Adds a user to the database.
    # Returns True if user added successfully, else False.
    try:
        me = Picture(bid, name, des, url)
        db.session.add(me)
        db.session.commit()
        return True

    except Exception as e:
        # Prints why the user could not be added in the terminal.
        print(e)
        return False





