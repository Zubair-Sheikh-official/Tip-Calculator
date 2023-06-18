# Tip Calculator

# Function to calculate the tip amount
def calculate_tip(total_amount, tip_percentage):
    tip_amount = total_amount * (tip_percentage / 100)
    return tip_amount

# Function to calculate the total bill including the tip
def calculate_total_bill(total_amount, tip_amount):
    total_bill = total_amount + tip_amount
    return total_bill

# Function to display the result
def display_result(total_amount, tip_percentage, tip_amount, total_bill):
    print("=== Tip Calculator Result ===")
    print("Total Amount: $", total_amount)
    print("Tip Percentage: ", tip_percentage, "%")
    print("Tip Amount: $", tip_amount)
    print("Total Bill: $", total_bill)

# Get the total bill amount from the user
total_amount = float(input("Enter the total amount: $"))

# Get the tip percentage from the user
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the tip amount
tip_amount = calculate_tip(total_amount, tip_percentage)

# Calculate the total bill
total_bill = calculate_total_bill(total_amount, tip_amount)

# Display the result
display_result(total_amount, tip_percentage, tip_amount, total_bill)