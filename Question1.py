# Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating 
# a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

while True:
    try: 
        temp_fahrenheit = float(input("Please enter a temperature in farenheit to convert to Celsius: "))
    except ValueError:
        print("Please enter a number.")
    else:
        break

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

def faren_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9


# Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

print(f"{temp_fahrenheit} degrees Fahrenheit is {faren_to_celsius(temp_fahrenheit)} degrees Celsius.")

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

def faren_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

def get_temp():
    while True:
        try: 
            temp_fahrenheit = float(input("Please enter a temperature in Fahrenheit to convert to Celsius: "))
            print(f"{temp_fahrenheit} degrees Fahrenheit is {faren_to_celsius(temp_fahrenheit)} degrees Celsius.")
        except ValueError:
            print("Please enter a number.")
        else:
            continue_input = input("Would you like to convert another temperature? (yes/no): ").lower()
            if continue_input != "yes":
                break
        finally:
            print("Thank you for using the weather forecast application!")

print("Welcome to the Weather Forecast application!")
get_temp()
