class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls,a,b):
        calculation_type = "Arithmetic Operations"
        print(f"Calculation type: {calculation_type}")
        return a * b