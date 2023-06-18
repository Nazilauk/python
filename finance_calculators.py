
#------------------------------------------------------------------------------------------------------------------------------
# Writing a program for a small financial company to access two financial calculators.
# This will include an investment calculator and a home loan repayment calculator.
#-------------------------------------------------------------------------------------------------------------------------------

import math

# Getting input from user on their choice of calculator i.e. investment or bond.
calculation_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed:
                            investment      - to calculate the amount of interest you'll earn on interest
                            bond            - to calculate the amount you'll have to pay on a home loan
                                               \n """)

# This will ensure that all options (e.g. Investment or investment etc.) are accepted into the conditional statement.
calculation_type = calculation_type.lower().replace(" ", "")

print()         # Blank line added for better presentation.

#---------------------------------------------------------------------------------------------------------------------------------
# conditional statement for investment calculator.
# Getting input from user on amount, rate, years and interest type to enter into investment calculator.
#----------------------------------------------------------------------------------------------------------------------------------
if calculation_type == "investment":

    deposit_amount = float(
        input("Please enter the amount of money you wish to deposit: \n"))
    interest_rate = int(
        input("Please enter your interest rate as a number (e.g. 1, 2, 3 etc.): \n"))
    num_years = int(
        input("Please enter the number of years you plan on investing for: \n"))
    interest_type = input(
        "Please enter your investment choice type: (simple or compound) \n")
#-----------------------------------------------------------------------------------------------------------------------------------
# Creating indented conditional statement to display the results based on user's choice of interest type.
# Entering formulas for simple and compound interest depending on user choice.
#-----------------------------------------------------------------------------------------------------------------------------------
    if interest_type.lower() == "simple":
        simple_interest = round(
            deposit_amount*(1 + (interest_rate/100) * num_years), 2)
        print()
        print("After {} years of investing at {}% interest rate, your return is:{}.".format(
            num_years, interest_rate, simple_interest))

    elif interest_type.lower() == "compound":
        compound_interest = round(
            deposit_amount * math.pow((1 + interest_rate/100), num_years), 2)
        print()
        print("After {} years of investing at {}% interest rate, your return is:{}.".format(
            num_years, interest_rate, compound_interest))
#------------------------------------------------------------------------------------------------------------------------------------
# conditional statement for bondcalculator.
# Getting input from user on house value, interest rate and number of months taken to pay bond, to enter into bond calculator.
#------------------------------------------------------------------------------------------------------------------------------------
elif calculation_type == "bond":

    house_value = int(input("Please enter the present value of the house: \n"))
    interest_rate = int(
        input("Please enter your interest rate as a number (e.g. 1, 2, 3 etc.): \n"))
    num_months = int(input(
        "Please enter the number of months you plan to take to repay the bond: \n"))

# Entering Formula for bond calculator.
    monthly_payment = round((interest_rate/100/12 * house_value) /
                            (1 - math.pow((1 + interest_rate/100/12), (-1 * num_months))), 2)

# Displaying monthly payment results.
    print("Your monthly repayment amount for the home loan is equal to: {}.".format(
        monthly_payment))

# Displaying error message if the user did not enter either 'investment' or 'bond' choice.

else:
    print("You have made an incorrect selection. Please choose either 'investment' or 'bond'.")
