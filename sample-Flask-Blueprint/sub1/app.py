from flask import Blueprint

sub1 = Blueprint('sub1', __name__)


@sub1.route('/')
def index():
    return "ok1"
