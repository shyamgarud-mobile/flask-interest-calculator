class InterestCalculator:
    @staticmethod
    def calculate_simple_interest(principal, rate, time_period):
        """
        Calculate simple interest amount and total amount
        
        Args:
            principal (float): The principal amount
            rate (float): Annual interest rate as a percentage
            time_period (int): Time period in months
            
        Returns:
            tuple: (interest_amount, total_amount)
        """
        # Convert annual rate to decimal and time period from months to years
        rate_decimal = rate / 100
        time_years = time_period / 12
        
        # Calculate simple interest: P × R × T
        interest_amount = principal * rate_decimal * time_years
        
        # Calculate total amount: P + I
        total_amount = principal + interest_amount
        
        return round(interest_amount, 2), round(total_amount, 2)