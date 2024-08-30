from flask import Flask, jsonify, request, render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Customer Model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)    
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)

# Create the database and table
with app.app_context():
    db.create_all()

# Routes to manage customers
@app.route('/', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        return render_template('index.html', customers=customers)
    except Exception as e:
        return str(e), 500

@app.route('/customers', methods=['GET'])
def get_customers_json():
    try:
        customers = Customer.query.all()
        return jsonify([{
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        } for customer in customers])
    except Exception as e:
        return str(e), 500

# Route to post data into customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        if not data:
            abort(400, description="No input data provided")
        
        new_customer = Customer(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address')
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer added successfully', 'customer_id': new_customer.id}), 201
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
