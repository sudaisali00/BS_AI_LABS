# ---------------------- TASK 01 ----------------------

# Ask the user for their full name
full_name = input("Enter your full name: ")

# Ask the user for their favorite color
favorite_color = input("Enter your favorite color: ")

# Ask the user for their birth year and convert it to integer
birth_year = int(input("Enter your birth year: "))

# Calculate age using the current year
current_year = 2026
age = current_year - birth_year

# Print personalized messages using f-strings
print(f"Welcome, {full_name}!")
print(f"Your favorite color is {favorite_color} – perfect for calm AI thinking.")
print(f"You were born in {birth_year} → you are currently {age} years old ({current_year}).")


# ---------------------- TASK 02 ----------------------

# Ask user for two numbers (float allows decimal numbers)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to enter the mathematical operation
operation = input("Enter operation (+ - * / ** %): ")

# Validate if the operation is allowed
if operation not in ["+", "-", "*", "/", "**", "%"]:
    print("Invalid operator!")

# Check division by zero
elif operation == "/" and num2 == 0:
    print("Cannot divide by zero!")

else:
    # Perform calculation based on the chosen operator
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")

    elif operation == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result:.2f}")

    elif operation == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")


# ---------------------- TASK 03 - Challenge A ----------------------

# Ask the user for starting and ending numbers
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Initialize the counter for the while loop
num = start

# Loop through numbers from start to end
while num <= end:

    # Skip numbers divisible by 7
    if num % 7 == 0:
        num += 1
        continue

    # Check if number is even and multiple of 5
    if num % 2 == 0 and num % 5 == 0:
        print(f"{num} → Even & Multiple of 5!!")

    # Check if number is even
    elif num % 2 == 0:
        print(f"{num} → Even")

    # Check if number is multiple of 5
    elif num % 5 == 0:
        print(f"{num} → Multiple of 5!")

    # If none of the conditions match
    else:
        print(num)

    num += 1


# ---------------------- TASK 03 - Challenge B ----------------------

# Ask the user to enter a password
password = input("Enter a password: ")

# Check if password length is less than 6
if len(password) < 6:
    print("Too short!")

else:
    # Check if password contains at least one digit
    has_digit = any(char.isdigit() for char in password)

    # Check if password contains at least one uppercase letter
    has_upper = any(char.isupper() for char in password)

    if not has_digit:
        print("Add at least one number")

    elif not has_upper:
        print("Add at least one capital letter")

    else:
        print("Strong password – good choice!")