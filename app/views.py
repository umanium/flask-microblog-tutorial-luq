__author__ = 'Luqman'

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname": "uman"}  # user palsu
    posts = [
        {
            "author": {"nickname": "sarala"},
            "body": "Hari ini cerah!!"
        },
        {
            "author": {"nickname": "serele"},
            "body": "Kabut asap di mana-mana T-T"
        }
    ]
    return render_template("index.html",
                           title="Home",
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("login requested for openID: '%s', remember me: %s" %
              (form.openid.data, str(form.remember_me.data)))
        return redirect("/index")
    return render_template("login.html",
                           title="Sign In",
                           form=form,
                           providers=app.config["OPENID_PROVIDERS"])