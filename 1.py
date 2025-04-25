
def divide_numbers(num1, num2):
    while True:
        try:
            result = num1 / num2
        except ZeroDivisionError as e:
            print(f"Error: Cannot divide by zero. ({e})")
        except TypeError as e:
            print(f"Error: Invalid input type. ({e})")
        else:
            print(f"The result is {result}")
        finally:
            print("Execution completed.")
            break


# Example usage
divide_numbers(10, 20)   # Valid division
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, 'a') # Invalid type for division
