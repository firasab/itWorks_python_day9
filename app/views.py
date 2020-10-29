import flask, flask_login
from . import app, db  
from . import forms
from .models import User


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    query_form = forms.QueryForm()
    if query_form.validate_on_submit():
        url = flask.url_for('search_users', username=query_form.query.data)
        return flask.redirect(url)
    else:
        print(query_form.errors)

    return flask.render_template("index.html", title="My awesome app", title2="Awesome app", query_form=query_form)

@app.route("/search-by/user/<username>")
def search_users(username):
    matching_users = list(User.query.filter_by(name=username))
    return flask.render_template("users_list.html", users=matching_users)

@app.route("/profile/<user_name>")
def profile_page(user_name):
    user = User.query.filter_by(name=user_name).first_or_404()
    return flask.render_template("profile_page.html", user=user)

@app.route("/users_list")
def users_list():
    users = User.query.all()
    return flask.render_template("users_list.html", users=users)

@app.route("/secret-page")
@flask_login.login_required
def secret():
    return "You reached the secret page !"

@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():

            user = User()
            user.name = form.username.data
            user.password = form.password.data

           
            user.save()

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    username = form.username.data
    password = form.password.data
    if form.validate_on_submit():
        user = User.login_user(username, password)
        if user:
            return flask.redirect('/')

    return flask.render_template("signin.html", form=form)

@app.route("/sign-out")
def signout():
    flask_login.logout_user()
    return flask.redirect('/')