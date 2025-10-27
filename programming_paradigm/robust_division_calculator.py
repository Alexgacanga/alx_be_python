def safe_divide(numerator, denominator):
    try:
        try:
            return f"The result of the division is {float(numerator) / float(denominator)}"
        except ValueError:
            return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."