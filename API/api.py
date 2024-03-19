from flask import Blueprint, render_template
import requests

import json


api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static')
URL_API = "https://fakestoreapi.com"

#Načte  seznam produktů z API v JSON formátu a vrátí jej jako pole.
def GetAllProducts():   
    
    request = requests.get(f"{URL_API}/products")
    
    return json.loads(request.text)

#Načte  seznam produktů z API v JSON formátu a vrátí jej jako pole.
def GetSingleProducts(id):   
    
    request = requests.get(f"{URL_API}/products/" + str(id))
    
    return json.loads(request.text)


def GetRelatedProducts(category):
    request = requests.get(f"{URL_API}general/category/", {category})
    products = json.loads(request.text)
    return products[:4] 
    
def get_category(category):
    response = requests.get(category)
    products = response.json()
    return render_template('general/index.html', categories = category)

#produkt n
def AddProduct(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{URL_API}/products", headers=headers, json=data)
    return response.json()

@api_bp.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    if not data:
        return json({'error': 'No data provided'}), 400
    
    if 'name' not in data or 'price' not in data:
        return json({'error': 'Name and price are required'}), 400
    
    new_product = AddProduct(data)
    if new_product:
        return json({'message': 'Product added successfully', 'product': new_product}), 201
    else:
        return json({'error': 'Failed to add product'}), 500