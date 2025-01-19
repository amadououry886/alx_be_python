# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    except Exception as e:
        # General error handling for unforeseen issues
        return f"Error: {str(e)}"


