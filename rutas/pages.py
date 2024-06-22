
from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/home')
def home():
    return render_template('home.html')
