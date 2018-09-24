from flask.helpers import make_response
from flask.templating import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    resp = make_response(
        render_template('main/index.html'))
    return resp
