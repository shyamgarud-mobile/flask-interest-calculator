# Flask Interest Calculator API Guide

This document explains how to use the Interest Calculator API endpoints.

## Setup Instructions

1. Create a MySQL database named `interest_calculator`
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Configure the database connection in `instance/config.py`
4. Run the application:
   ```
   python run.py
   ```

## API Endpoints

### 1. Calculate Interest (without saving to database)

**Endpoint:** `POST /api/loans/calculate`

**Description:** Calculate simple interest without creating a database record

**Request Body:**
```json
{
  "principal": 1000,
  "rate": 5.5,
  "time_period": 12
}
```

**Response:**
```json
{
  "result": {
    "principal": 1000,
    "rate": 5.5,
    "time_period": 12,
    "interest_amount": 55.0,
    "total_amount": 1055.0
  }
}
```

### 2. Create a Loan Record

**Endpoint:** `POST /api/loans/`

**Description:** Create a new loan record with calculated interest

**Request Body:**
```json
{
  "principal": 5000,
  "rate": 4.5,
  "time_period": 24
}
```

**Response:**
```json
{
  "loan": {
    "id": 1,
    "principal": 5000.0,
    "rate": 4.5,
    "time_period": 24,
    "interest_amount": 450.0,
    "total_amount": 5450.0,
    "created_at": "2025-05-07T12:00:00.000000",
    "updated_at": "2025-05-07T12:00:00.000000"
  }
}
```

### 3. Get All Loans

**Endpoint:** `GET /api/loans/`

**Description:** Get all loan records

**Response:**
```json
{
  "loans": [
    {
      "id": 1,
      "principal": 5000.0,
      "rate": 4.5,
      "time_period": 24,
      "interest_amount": 450.0,
      "total_amount": 5450.0,
      "created_at": "2025-05-07T12:00:00.000000",
      "updated_at": "2025-05-07T12:00:00.000000"
    },
    {
      "id": 2,
      "principal": 10000.0,
      "rate": 3.0,
      "time_period": 36,
      "interest_amount": 900.0,
      "total_amount": 10900.0,
      "created_at": "2025-05-07T12:30:00.000000",
      "updated_at": "2025-05-07T12:30:00.000000"
    }
  ]
}
```

### 4. Get a Specific Loan

**Endpoint:** `GET /api/loans/<loan_id>`

**Description:** Get a specific loan by ID

**Response:**
```json
{
  "loan": {
    "id": 1,
    "principal": 5000.0,
    "rate": 4.5,
    "time_period": 24,
    "interest_amount": 450.0,
    "total_amount": 5450.0,
    "created_at": "2025-05-07T12:00:00.000000",
    "updated_at": "2025-05-07T12:00:00.000000"
  }
}
```

### 5. Update a Loan

**Endpoint:** `PUT /api/loans/<loan_id>`

**Description:** Update an existing loan record (interest will be recalculated automatically)

**Request Body:**
```json
{
  "principal": 6000,
  "rate": 5.0
}
```

**Response:**
```json
{
  "loan": {
    "id": 1,
    "principal": 6000.0,
    "rate": 5.0,
    "time_period": 24,
    "interest_amount": 600.0,
    "total_amount": 6600.0,
    "created_at": "2025-05-07T12:00:00.000000",
    "updated_at": "2025-05-07T13:00:00.000000"
  }
}
```

### 6. Delete a Loan

**Endpoint:** `DELETE /api/loans/<loan_id>`

**Description:** Delete a loan record

**Response:**
```json
{
  "message": "Loan deleted successfully"
}
```

## Interest Calculation Formula

The application uses the simple interest formula:

```
Interest = Principal × Rate × Time
```

Where:
- Principal: The initial amount of money
- Rate: Annual interest rate (as a decimal, e.g., 5% = 0.05)
- Time: Time period in years (months/12)

The total amount is calculated as:

```
Total Amount = Principal + Interest
```