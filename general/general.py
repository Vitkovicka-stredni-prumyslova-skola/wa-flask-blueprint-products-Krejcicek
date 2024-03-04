from flask import Blueprint, render_template

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    static_folder='static')

@general_bp.route('/')
def index():
    return render_template('general/index.html')

@general_bp.route('/categories')
def display_categories():
    categories = ['bundy', 'kalhoty', 'prsteny']
    return render_template('general/categories/index.html', categories=categories)