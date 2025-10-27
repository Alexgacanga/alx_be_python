def safe_divide(numerator, denominator):
    try:
        try:
            return f"The result of the division is {float(numerator) / float(denominator)}"
        except ValueError:
            print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")