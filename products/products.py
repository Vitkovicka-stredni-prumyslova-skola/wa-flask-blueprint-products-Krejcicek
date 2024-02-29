from flask import Blueprint, render_template
from API.api import GetAllProducts, GetSingleProducts, GetRelatedProducts
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    
    return render_template('products/products.html', length = l, products = data)

@products_bp.route('/products/<int:id>')
def detailOfProduct(id):
    data = GetSingleProducts(id)

    return render_template('products/detail.html', detailOfPorduct = data, relatedProducts = related_products)
