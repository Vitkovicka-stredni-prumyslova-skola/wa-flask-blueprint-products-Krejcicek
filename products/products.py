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
    related_products = GetRelatedProducts(data['category'])

    return render_template('products/detail.html', detailOfPorduct = data, RelatedProducts = related_products)

products_bp.route('/products/add')
def addProduct():
    return render_template('products/new-product.html')




@products_bp.route('/products/add', methods=['GET', 'POST'])
def addProduct():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'price': request.form.get('price'),
            'category': request.form.get('category'),
            
        }
     
        new_product = AddProduct(data)
        if new_product:
            return redirect(url_for('products_bp.index'))  
        else:
            return render_template('error.html', message='Failed to add product') 
    else:
        return render_template('products/new-product.html')  u