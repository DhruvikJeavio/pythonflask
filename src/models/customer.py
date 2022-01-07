import json

from inc.db import db
 
class Customer(db.Model):
    """Customer model

    Args:
        db (class): model
    """
    __tablename__='customers'
    __table_args__ = {'extend_existing': True}


    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    profile = db.Column(db.String(80),nullable=False)
    company = db.Column(db.String(80),nullable=False)
    team = db.Column(db.String(80),nullable=True)
    def json(self):
        return {'id': self.id, 'name': self.name,
                'profile': self.profile, 'company': self.company,
                'team':self.team}
