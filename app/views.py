from flask import Blueprint, render_template, request, redirect, url_for, flash
from .controllers import ProductController

product_bp = Blueprint('product', __name__)


@product_bp.route('/')
def index():
    products = ProductController.get_all_products()
    shopping_list = ProductController.get_shopping_list()
    return render_template('index.html', products=products, shopping_list=shopping_list)


@product_bp.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = request.form['quantity']
    success, message = ProductController.add_product(name, quantity)
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    return redirect(url_for('product.index'))


@product_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    products = ProductController.search_products(query)
    return render_template('search_results.html', products=products, query=query)


@product_bp.route('/update_product', methods=['POST'])
def update_product():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    is_valid, error_message = ProductController.validate_product("dummy", quantity)
    if is_valid:
        ProductController.update_product(product_id, int(quantity))
        flash('המוצר עודכן בהצלחה', 'success')
    else:
        flash(error_message, 'error')
    return redirect(url_for('product.index'))


@product_bp.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    ProductController.delete_product(product_id)
    flash('המוצר נמחק בהצלחה', 'success')
    return redirect(url_for('product.index'))

