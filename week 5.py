CONVERSION_FACTOR=0.6214

def main():
    #Get the distance in kilometers.
    kilometers=float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
        #Calculate miles.
        miles = km * CONVERSION_FACTOR
        
        #Display the miles.
        print(km,'kilometers equals', miles, 'miles')

main()

#Redisgn the program from chapter 2 that calculates and displays the county and state sales tax on a purchase
#Redisn it so the subtask are in functions
state_tax_rate = 0.05
county_tax_rate = 0.025

def calculate_state_tax(purchase_amount):
    return purchase_amount * state_tax_rate

def calculate_county_tax(purchase_amount):
    return purchase_amount * county_tax_rate

def calculate_total_sales_tax(state_tax, county_tax):
    return state_tax + county_tax

def calculate_total_cost(purchase_amount, total_sales_tax):
    return purchase_amount + total_sales_tax

def display_results(purchase_amount, state_tax, county_tax, total_sales_tax, total_cost):
    print(f'Amount of purchase: ${purchase_amount:.2f}')
    print(f'State sales tax: ${state_tax:.2f}')
    print(f'County sales tax: ${county_tax:.2f}')
    print(f'Total sales tax: ${total_sales_tax:.2f}')
    print(f'Total amount (including taxes): ${total_cost:.2f}')

def main():
    purchase_amount = float(input("Enter the amount of the purchase: "))
    
    state_tax = calculate_state_tax(purchase_amount)
    county_tax = calculate_county_tax(purchase_amount)
    total_sales_tax = calculate_total_sales_tax(state_tax, county_tax)
    total_cost = calculate_total_cost(purchase_amount, total_sales_tax)
    
    display_results(purchase_amount, state_tax, county_tax, total_sales_tax, total_cost)

main()


#Write a program that ask the user to enter the replacement cost of a building, then displays the min of insurance he or she should buy for the property.
def calculate_minimum_insurance(replacement_cost):
    """Calculate the minimum amount of insurance needed."""
    return replacement_cost * 0.80

def main():
    
    try:
        replacement_cost = float(input("Enter the replacement cost of the building: $"))
        if replacement_cost < 0:
            print("The replacement cost cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Calculate the minimum amount of insurance
    minimum_insurance = calculate_minimum_insurance(replacement_cost)
    
    # Display the result
    print(f"The minimum amount of insurance you should buy is: ${minimum_insurance:.2f}")

main()


# Write a program that asks the user to enter the monthly costs for the following expenses incurred from operationg their automobile
#Loan payment, insurance, gas, oil, tires, and maintenance
#The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses
def main():
    print("Enter your monthly costs for the following expenses:")
    
    # Prompt user for each expense
    loan_payment = float(input("Loan Payment: $"))
    insurance = float(input("Insurance: $"))
    gas = float(input("Gas: $"))
    oil = float(input("Oil: $"))
    tires = float(input("Tires: $"))
    maintenance = float(input("Maintenance: $"))
    
    # Calculate total monthly cost
    total_monthly_cost = (loan_payment + insurance + gas + 
                           oil + tires + maintenance)
    
    # Calculate total annual cost
    total_annual_cost = total_monthly_cost * 12
    
    # Display the results
    print("\nTotal Monthly Cost: ${:.2f}".format(total_monthly_cost))
    print("Total Annual Cost: ${:.2f}".format(total_annual_cost))

main()


#Write a program that ask the actual value of a piece of property and displays the assessment value and property tax.
def main():
   
    actual_value = float(input("Enter the actual value of the property: $"))

    
    assessment_value = actual_value * 0.60

    
    property_tax_rate = 0.72 / 100  
    property_tax = assessment_value * property_tax_rate * 100  

    
    print(f"\nAssessment Value: ${assessment_value:.2f}")
    print(f"Property Tax: ${property_tax:.2f}")

main()


#Write a program that ask how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.

def main():
    
    class_a_price = 20
    class_b_price = 15
    class_c_price = 10
    
    
    class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets = int(input("Enter the number of Class C tickets sold: "))
    
   
    total_income_a = class_a_tickets * class_a_price
    total_income_b = class_b_tickets * class_b_price
    total_income_c = class_c_tickets * class_c_price
    
    total_income = total_income_a + total_income_b + total_income_c
    
   
    print(f"\nTotal income from Class A tickets: ${total_income_a:.2f}")
    print(f"Total income from Class B tickets: ${total_income_b:.2f}")
    print(f"Total income from Class C tickets: ${total_income_c:.2f}")
    print(f"\nTotal income generated from ticket sales: ${total_income:.2f}")

main()


#Write a program that ask the user to enter the square feet of wall space to be painted and the price of the paint per gallon.
#The program should display the following:

def calculate_paint_job():
    
    SQUARE_FEET_PER_GALLON = 112
    LABOR_HOURS_PER_GALLON = 8
    LABOR_RATE_PER_HOUR = 35.00

   
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    paint_price_per_gallon = float(input("Enter the price of the paint per gallon: "))

   
    gallons_required = square_feet / SQUARE_FEET_PER_GALLON
    labor_hours_required = gallons_required * LABOR_HOURS_PER_GALLON
    cost_of_paint = gallons_required * paint_price_per_gallon
    labor_charges = labor_hours_required * LABOR_RATE_PER_HOUR
    total_cost = cost_of_paint + labor_charges

   
    
    print(f"Gallons of paint required: {gallons_required:.2f}")#The number of gallons of paint required
    print(f"Hours of labor required: {labor_hours_required:.2f}")#The hours of labor required 
    print(f"Cost of paint: ${cost_of_paint:.2f}")#The cost of the paint
    print(f"Labor charges: ${labor_charges:.2f}")#The labor charges
    print(f"Total cost of the paint job: ${total_cost:.2f}")#The total cost of the paint job


calculate_paint_job()


#Write a program that ask the user to enter the total sales for the month. 
def calculate_sales_tax():
   
    STATE_TAX_RATE = 0.05 
    COUNTY_TAX_RATE = 0.025  

 
    total_sales = float(input("Enter the total sales for the month: "))

   
    county_sales_tax = total_sales * COUNTY_TAX_RATE
    state_sales_tax = total_sales * STATE_TAX_RATE
    total_sales_tax = county_sales_tax + state_sales_tax

    print(f"Total Sales: ${total_sales:.2f}")
    print(f"County Sales Tax: ${county_sales_tax:.2f}")#The amount of county sales tax
    print(f"State Sales Tax: ${state_sales_tax:.2f}")#The amount of state sales tax
    print(f"Total Sales Tax: ${total_sales_tax:.2f}")#The total sales tax


calculate_sales_tax()


#Constqant for the number of inches per foot.
INCHES_PER_FOOT=12
#main function
def main():
    #Get a number of feet from the user.
    feet=int(input('Enter a number of feet: '))

    #Covert that to inches.
    print(feet, 'equals',feet_to_inches(feet), 'inches.')
#The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()


#Write a program that gives simple math quizzes. The program should display two random numbers that are to be added, such ass 247 + 129

import random

def math_quiz():
    
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)

    print(f"\nWhat is {num1} + {num2}?")
    
    user_answer = input("Your answer: ")#The program should allow the student to enter the answer. 

    correct_answer = num1 + num2
    
    if user_answer.isdigit() and int(user_answer) == correct_answer:
        print("Correct!")#If the answer is correctm a message of congrats should be displayed 
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")#If the answer is incorrect, a message showing the correct answers should be displayed.


math_quiz()

