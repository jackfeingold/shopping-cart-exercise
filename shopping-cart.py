# shopping_cart.py
# code for Jack Feingold OPIM 243

from math import prod


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

# input validation setup

product_ids = []
for x in products:
    product_ids.append(str(x["id"]))



# ask for user input

# ASK FOR USER INPUT

purchased_items = []

while True:
    product_id = input("Please input a product identifier or 'DONE': ")
    #print(product_id) #> "9"
    #print(type(product_id)) #> str

    if product_id == "DONE":
        break
    
    # LOOK UP CORRESPONDING PRODUCTS

    # print product that has an id attribute equal to "9"

    if product_id not in product_ids:
        print("Item not found.  Please ensure you have entered a valid ID.")

    for x in products:
        #if x == 3:
        #    ___.append(x)
        #print(x)
        #print(x["id"])
        if str(x["id"]) == str(product_id):
            # this is a match
            purchased_items.append(x)
        

#print(purchased_items)

#for x in purchased_items:
#    print(x.keys())

# loop cooresponding products

# compile receipt

import time
local_time = time.localtime()



print(" ")
print("FITZGERALD'S FINE FOODS")
print("WWW.FITZGERALDS.COM")
print(time.strftime('%a, %d %b %Y %H:%M:%S', local_time))
print("----------------------")
print(" ")


subtotal = 0

for x in purchased_items:
    print("...." + x["name"], "${:,.2f}".format(x["price"]))
    subtotal = subtotal + x["price"]

# Tax rate subject to change
tax = 0.0875 * subtotal

total = subtotal + tax

print(" ")
print("----------------------")
print("....Subtotal:", "${:,.2f}".format(subtotal))
print("....Tax (8.75%):", "${:,.2f}".format(tax))
print("....Total:", "${:,.2f}".format(total))
print(" ")
print("Thank you for your business!")






# print receipt
