# SETUP CELL
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


def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output


#ask for user input
#input product identifier
#datetime functions with help from progamiz
from datetime import date
today = date.today()
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M %p")





#selected_ids = []
selected_products = []




while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items:")
    #print(product_id)
    #look up corresponding products
    if product_id == "DONE":
        break

    #matching_products = [] 
    for x in products:
        if str(x["id"]) == str(product_id): #this is a match
            selected_products.append(x)
            #matching_products.append(x)
print("Here's your receipt:")
print("----------------------")
print("WHOLE FOODS")
print("WWW.WHOLE-FOODS.COM")
print("----------------------")
print("CHECKOUT AT:", dt_string)
total_price = 0
#tax = 0
#grand_total = 0
#print(selected_products)
for selected_product in selected_products:
    print(selected_product["name"], selected_product["price"])
    total_price = total_price + selected_product["price"]

print(to_usd(total_price))
tax = total_price * 0.3
grand_total = total_price + tax
print(to_usd(tax))
print(to_usd(grand_total))

#print("SELECTED PRODUCT: ")
#print(matching_product["name"] + " " + str(matching_product["price"]))
print("----------------------")
print("SUBTOTAL: " + '$' + format(total_price, '.2f')) #got this from stack overflow
print("TAX: " + '$' + format(tax, '.2f'))
print("TOTAL: " + '$' + format(grand_total, '.2f'))
print("----------------------")
print("THANK YOU, SEE YOU AGAIN SOON!")
print("----------------------")

