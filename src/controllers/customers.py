"""customers module contains customer functions
"""
import re
from flask import  jsonify,request,Response
from flask.views import MethodView
from models import customer
from models.customer import Customer
from inc.db import db
def hello_world():
    """hello_world returns  html response

    Returns:
        [html]: [response]
    """
    return "<h2>For documentation :- /api/docs </h2>"
   

class CustomerAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            # return a list of users
            
            return jsonify({
                'Customers':[Customer.json(customer) for customer in Customer.query.all()]
            })
            
        else:
            customer=Customer.query.filter_by(id=user_id).first()
            if customer==None:
                return Response("No such customer found", 406, mimetype='application/json')
                
            return jsonify(
                customer
            )
            # expose a single user

    def post(self):
        # create a new user
        data = request.get_json()
        print(data)
        new_customer = Customer(name=data["name"],profile=data["profile"],company=data["company"],team=data["team"])
        db.session.add(new_customer)
        db.session.commit()
        response = Response("Customer added", 201, mimetype='application/json')
        return response
        

    def delete(self, user_id):
        # delete a single user
        if Customer.query.filter_by(id=user_id).first()== None :
            return Response("No such customer ID found",406,mimetype='application/json')
        Customer.query.filter_by(id=user_id).delete()

        db.session.commit()
        response = Response("Customer deleted", 201, mimetype='application/json')
        return response

    def put(self, user_id):
        # update a single user
        data = request.get_json()
        customer_to_update = Customer.query.filter_by(id=user_id).first()
        if customer_to_update==None:
            return Response("No such customer found", 406, mimetype='application/json')

        customer_to_update.name = data["name"]
        customer_to_update.profile = data["profile"]
        customer_to_update.company = data["company"]
        customer_to_update.team = data["team"]

        db.session.commit()
        response = Response("Customer updated", 201, mimetype='application/json')
        return response


    


    
