from flask import Blueprint

sub2 = Blueprint('sub2', __name__)


@sub2.route('/')
def index():
    return "ok2"
