from app import db
from app.models.loan import Loan

class LoanRepository:
    @staticmethod
    def get_all():
        """Get all loans from the database"""
        return Loan.query.all()
    
    @staticmethod
    def get_by_id(loan_id):
        """Get a loan by ID"""
        return Loan.query.get(loan_id)
    
    @staticmethod
    def create(principal, rate, time_period, interest_amount=None, total_amount=None):
        """Create a new loan record"""
        loan = Loan(principal=principal, rate=rate, time_period=time_period)
        if interest_amount is not None:
            loan.interest_amount = interest_amount
        if total_amount is not None:
            loan.total_amount = total_amount
        
        db.session.add(loan)
        db.session.commit()
        return loan
    
    @staticmethod
    def update(loan_id, data):
        """Update an existing loan record"""
        loan = LoanRepository.get_by_id(loan_id)
        if not loan:
            return None
        
        for key, value in data.items():
            if hasattr(loan, key):
                setattr(loan, key, value)
        
        db.session.commit()
        return loan
    
    @staticmethod
    def delete(loan_id):
        """Delete a loan by ID"""
        loan = LoanRepository.get_by_id(loan_id)
        if not loan:
            return False
        
        db.session.delete(loan)
        db.session.commit()
        return True