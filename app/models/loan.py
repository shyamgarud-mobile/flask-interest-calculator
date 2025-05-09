from app import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'
    
    id = db.Column(db.Integer, primary_key=True)
    principal = db.Column(db.Float, nullable=False)
    rate = db.Column(db.Float, nullable=False)  # Annual interest rate (percentage)
    time_period = db.Column(db.Integer, nullable=False)  # Time period in months
    interest_amount = db.Column(db.Float, nullable=True)
    total_amount = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, principal, rate, time_period):
        self.principal = principal
        self.rate = rate
        self.time_period = time_period
    
    def to_dict(self):
        return {
            'id': self.id,
            'principal': self.principal,
            'rate': self.rate,
            'time_period': self.time_period,
            'interest_amount': self.interest_amount,
            'total_amount': self.total_amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }