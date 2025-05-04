from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import Product
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@admin_bp.route('/add', methods=['POST'])
@login_required
def add_product():
    product = Product(name=request.form['name'], description=request.form['description'], price=request.form['price'])
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('admin.dashboard'))
