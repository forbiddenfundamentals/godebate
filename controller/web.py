from flask import Blueprint, render_template

WEB_PREFIX = 'web'

web = Blueprint(WEB_PREFIX, __name__)


@web.route('/')
def index():
    return render_template("index.html")
