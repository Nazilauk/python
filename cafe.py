# ---------------------------------------------------------------------------------------------------
# cafe.py
# Creates a list called menu, which should contain at least 4 items in the cafe.
# creates a dictionary called stock, which should contain the stock
# value for each item on your menu.
# Creates another dictionary called price, which should contain the prices for each item on the menu.
# calculates the total_stock worth in the cafe
# ---------------------------------------------------------------------------------------------------
# Create a list called menu
menu = ["coffee", "tea", "muffins", "cake"]

# create a dictionary called stock that contains the stock value for each item in the menu
stock = {"coffee": 10, "tea": 20, "muffins": 30, "cake": 40}

# create second dictionary called price that contains the prices for each item in the menu:
price = {"coffee": 2.50, "tea": 1.50, "muffins": 3.00, "cake": 4.00}

# Declare a variable "total_stock_worth" and initialize it to zero
total_stock_worth = 0

# Loop through each item in the "menu" list
for item in menu:
    # ------------------------------------------------------------------------------------------------------
    # Multiply the current item's stock quantity from the "stock" dictionary
    # with its respective price from the "price" dictionary and assign the result to variable "item_value"
    # ------------------------------------------------------------------------------------------------------
    item_value = stock[item] * price[item]
# Add the current item's value to the running total of all items' values
    total_stock_worth += item_value
# print total stock worth
print("Total stock worth of cafe items: $", total_stock_worth)
