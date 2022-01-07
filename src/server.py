"""
    app module deals with server configs
"""

from os import POSIX_FADV_DONTNEED
from flask import Flask,render_template
from inc.db import db
from controllers.customers import CustomerAPI,hello_world
from flask_migrate import Migrate, migrate
from models import customer
app = Flask(__name__)
app.config.from_object('config')

#database models 
db.init_app(app)
customer.Customer
migrate = Migrate(app,db)


##routes
@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('index.html')

    
app.add_url_rule("/",view_func= hello_world)
customer_view = CustomerAPI.as_view('customer_api')

app.add_url_rule("/api/customers",defaults={'user_id': None},view_func=customer_view,methods=["GET",])
app.add_url_rule("/api/customer",view_func=customer_view,methods=["POST",])
app.add_url_rule("/api/customer/<int:user_id>",view_func=customer_view,methods=["GET","PUT","DELETE"])

