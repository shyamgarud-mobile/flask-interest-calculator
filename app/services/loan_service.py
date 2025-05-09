from app.repositories.loan_repository import LoanRepository
from app.utils.calculator import InterestCalculator

class LoanService:
    @staticmethod
    def get_all_loans():
        """Get all loans with formatted data"""
        loans = LoanRepository.get_all()
        return [loan.to_dict() for loan in loans]
    
    @staticmethod
    def get_loan(loan_id):
        """Get a specific loan by ID"""
        loan = LoanRepository.get_by_id(loan_id)
        if not loan:
            return None
        return loan.to_dict()
    
    @staticmethod
    def create_loan(principal, rate, time_period):
        """Create a new loan with calculated interest"""
        # Calculate interest and total amount
        interest_amount, total_amount = InterestCalculator.calculate_simple_interest(
            principal, rate, time_period
        )
        
        # Save to database with calculated values
        loan = LoanRepository.create(
            principal=principal,
            rate=rate,
            time_period=time_period,
            interest_amount=interest_amount,
            total_amount=total_amount
        )
        
        return loan.to_dict()
    
    @staticmethod
    def update_loan(loan_id, data):
        """Update a loan and recalculate interest if necessary"""
        loan = LoanRepository.get_by_id(loan_id)
        if not loan:
            return None
        
        # If any of the calculation factors are being updated, recalculate interest
        recalculate = any(key in data for key in ['principal', 'rate', 'time_period'])
        
        if recalculate:
            # Use new values if provided, otherwise use existing values
            principal = data.get('principal', loan.principal)
            rate = data.get('rate', loan.rate)
            time_period = data.get('time_period', loan.time_period)
            
            # Calculate new interest and total values
            interest_amount, total_amount = InterestCalculator.calculate_simple_interest(
                principal, rate, time_period
            )
            
            # Add calculated values to data for update
            data['interest_amount'] = interest_amount
            data['total_amount'] = total_amount
        
        # Update the loan with all data
        updated_loan = LoanRepository.update(loan_id, data)
        if not updated_loan:
            return None
        
        return updated_loan.to_dict()
    
    @staticmethod
    def delete_loan(loan_id):
        """Delete a loan by ID"""
        return LoanRepository.delete(loan_id)
    
    @staticmethod
    def calculate_interest(principal, rate, time_period):
        """Calculate interest without creating a database record"""
        interest_amount, total_amount = InterestCalculator.calculate_simple_interest(
            principal, rate, time_period
        )
        
        return {
            'principal': principal,
            'rate': rate,
            'time_period': time_period,
            'interest_amount': interest_amount,
            'total_amount': total_amount
        }