# Postman Collection Usage Guide

I've created two files for easy API testing with Postman:

1. `interest_calculator_postman_collection.json` - The API collection with all endpoints
2. `interest_calculator_environment.json` - Environment variables for local testing

## How to Import the Collection and Environment

1. Open Postman
2. Click on "Import" in the top left corner
3. Drag and drop both JSON files or use the file selection dialog
4. Both the collection and environment will be imported

## Setting Up the Environment

1. After importing, click on the environment dropdown in the top right corner
2. Select "Interest Calculator Local" environment
3. The `base_url` variable is already set to `http://localhost:5000`
4. You can adjust this if your Flask app is running on a different port or host

## Using the Collection

The collection includes the following requests:

### 1. Calculate Interest
- Calculates simple interest without saving to the database
- Modify the request body to test different values

### 2. Create Loan
- Creates a new loan record in the database with calculated interest
- The response will include the newly created record with ID

### 3. Get All Loans
- Retrieves all loan records from the database
- No parameters required

### 4. Get Loan by ID
- Retrieves a specific loan by ID
- Replace the `1` in the URL with the actual loan ID

### 5. Update Loan
- Updates an existing loan with new values
- Interest is automatically recalculated
- Replace the `1` in the URL with the actual loan ID

### 6. Delete Loan
- Deletes a loan record from the database
- Replace the `1` in the URL with the actual loan ID

## Suggested Testing Workflow

1. Start your Flask application: `python run.py`
2. Use "Calculate Interest" to verify the calculation logic
3. Create a few loans using "Create Loan" with different values
4. Use "Get All Loans" to verify the records were created
5. Get specific loans using "Get Loan by ID"
6. Update some loans using "Update Loan"
7. Delete a loan using "Delete Loan"

## Using Environment Variables

The collection uses the `{{base_url}}` environment variable, which allows you to easily switch between different environments (local, development, production) without modifying each request.

## Testing Automation

You can also add test scripts to each request by going to the "Tests" tab. For example:

```javascript
// Test for successful creation
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

// Test for correct JSON response
pm.test("Response has correct structure", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('loan');
    pm.expect(jsonData.loan).to.have.property('id');
});

// Store the created loan ID for later use
pm.test("Store loan ID", function () {
    var jsonData = pm.response.json();
    pm.environment.set("loan_id", jsonData.loan.id);
});
```

This way, you can create automated test sequences and reuse values like loan IDs across requests.
