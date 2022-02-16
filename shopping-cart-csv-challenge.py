# shopping-cart-csv-challenge.py
# code for Jack Feingold OPIM 243
# CSV Import challenge

from math import prod
from pandas import read_csv
from pandas import DataFrame

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


new_data = input("Update product data from CSV? This will overwrite existing product list. Enter y or n: ")

if new_data == "y" or new_data == "Y":
    filepath = input("Enter the filepath of the products file you would like to use.  MUST BE CSV: ")
    file_import = read_csv(filepath)
    products = file_import.to_dict("records")
    #for x in products:
    #    print(x.keys())






# input validation setup
# a list of all available product IDs will allow the program to quickly check valid inputs
product_ids = []
for x in products:
    product_ids.append(str(x["id"]))



# ask for user input

# inputs will be added to a list which will later be used
purchased_items = []

while True:
    product_id = input("Please input a product identifier or 'DONE': ")

    # breaks input loop if user enters the DONE keyword
    if product_id == "DONE":
        break
    
    # checks validity of input and alerts user if something other than an accepted input has been entered
    if product_id not in product_ids:
        print("Item not found.  Please ensure you have entered a valid ID and do not use punctuation.")

    # adds the appropriate product to the list of purchases
    for x in products:
        if str(x["id"]) == str(product_id):
            purchased_items.append(x)
        

# compile receipt

# create date and time to print on receipt
import time
local_time = time.localtime()


# heading of receipt displaying name of store, website, and date and time
print(" ")
print("FITZGERALD'S FINE FOODS")
print("WWW.FITZGERALDS.COM")
print(time.strftime('%a, %d %b %Y %H:%M:%S', local_time))
print("----------------------")
print(" ")


# a running subtotal will be calculated as the names and prices of items are printed out
subtotal = 0

# prints the name of the item and the price formatted as $0.00 and adds each item to the subtotal
for x in purchased_items:
    print("...." + x["name"], "${:,.2f}".format(x["price"]))
    subtotal = subtotal + x["price"]

# calculates tax based on 8.75% tax rate
tax = 0.0875 * subtotal

# total is simply the subtotal plus the taxes calculated above
total = subtotal + tax

# some formatting and the subtotal, taxes, and total printed in $0.00 format
# thank you message thanking the customer for their business
print(" ")
print("----------------------")
print("....Subtotal:", "${:,.2f}".format(subtotal))
print("....Tax (8.75%):", "${:,.2f}".format(tax))
print("....Total:", "${:,.2f}".format(total))
print(" ")
print("Thank you for your business!")



