from Cuterest import *

class Form_Login(Form):
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@app.route("/signin", methods=['GET','POST'])
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # Loading this page, send back the form
        return render_template('login.html')


    # The form has been filled out, process input.
    email = request.form['email']
    password = request.form['password']

    # Find the user with the given email address
    registered_user = User.query.filter_by(email=email).first()

    if registered_user is not None:
        # A user with the given email was found.
        if not registered_user.check_password(password):
            # wrong password
            print("User password does not match", password)
            return redirect(url_for('login'))
    else:
        # No user with the given email was found.
        print("No such user " + email)
        return redirect(url_for('login'))

    login_user(registered_user)
    try:
        # Allows a redirect to the requested page (if applicable) after login
        next = request.args.get('next')
    except:
        next = url_for('viewuserboards')
    return redirect(next or url_for('viewuserboards'))
