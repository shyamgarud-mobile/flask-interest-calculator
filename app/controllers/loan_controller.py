from flask import Blueprint, request, jsonify
from app.services.loan_service import LoanService

loan_bp = Blueprint('loans', __name__, url_prefix='/api/loans')

@loan_bp.route('/', methods=['GET'])
def get_all_loans():
    """Get all loans"""
    loans = LoanService.get_all_loans()
    return jsonify({'loans': loans}), 200

@loan_bp.route('/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    """Get a specific loan by ID"""
    loan = LoanService.get_loan(loan_id)
    if not loan:
        return jsonify({'error': 'Loan not found'}), 404
    return jsonify({'loan': loan}), 200

@loan_bp.route('/', methods=['POST'])
def create_loan():
    """Create a new loan"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['principal', 'rate', 'time_period']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        principal = float(data['principal'])
        rate = float(data['rate'])
        time_period = int(data['time_period'])
        
        if principal <= 0 or rate <= 0 or time_period <= 0:
            return jsonify({'error': 'Values must be positive numbers'}), 400
            
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid data types. Principal and rate must be numbers, time_period must be an integer'}), 400
    
    loan = LoanService.create_loan(principal, rate, time_period)
    return jsonify({'loan': loan}), 201

@loan_bp.route('/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    """Update an existing loan"""
    data = request.get_json()
    
    # Validate data types if provided
    try:
        if 'principal' in data:
            data['principal'] = float(data['principal'])
            if data['principal'] <= 0:
                return jsonify({'error': 'Principal must be a positive number'}), 400
                
        if 'rate' in data:
            data['rate'] = float(data['rate'])
            if data['rate'] <= 0:
                return jsonify({'error': 'Rate must be a positive number'}), 400
                
        if 'time_period' in data:
            data['time_period'] = int(data['time_period'])
            if data['time_period'] <= 0:
                return jsonify({'error': 'Time period must be a positive integer'}), 400
                
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid data types'}), 400
    
    updated_loan = LoanService.update_loan(loan_id, data)
    if not updated_loan:
        return jsonify({'error': 'Loan not found'}), 404
    
    return jsonify({'loan': updated_loan}), 200

@loan_bp.route('/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    """Delete a loan"""
    result = LoanService.delete_loan(loan_id)
    if not result:
        return jsonify({'error': 'Loan not found'}), 404
    
    return jsonify({'message': 'Loan deleted successfully'}), 200

@loan_bp.route('/calculate', methods=['POST'])
def calculate_interest():
    """Calculate interest without creating a database record"""
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['principal', 'rate', 'time_period']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    try:
        principal = float(data['principal'])
        rate = float(data['rate'])
        time_period = int(data['time_period'])
        
        if principal <= 0 or rate <= 0 or time_period <= 0:
            return jsonify({'error': 'Values must be positive numbers'}), 400
            
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid data types. Principal and rate must be numbers, time_period must be an integer'}), 400
    
    result = LoanService.calculate_interest(principal, rate, time_period)
    return jsonify({'result': result}), 200