# Data stored in Dictionaries
products_price = {
    "Sankofa Foods": 30,
    "Jamestown Coffee": 25,
    "Bioko Chocolate": 40,
    "Blue Skies Ice Cream": 20,
    "Fair Afric Chocolate": 20,
    "Kawa Moka Coffee": 35,
    "Aphro Spirit": 45,
    "Mensado Bissap": 50,
    "Voltic": 35
}

customer_purchases = {
    "Sankofa Foods": 2,
    "Jamestown Coffee": 3,
    "Bioko Chocolate": 5,
    "Blue Skies Ice Cream": 8,
    "Fair Afric Chocolate": 4,
    "Kawa Moka Coffee": 4,
    "Aphro Spirit": 6,
    "Mensado Bissap": 2,
    "Voltic": 9
}

# FUNTIONS OF THE CALCULATOR
# Calculate the total price average for all products
def total_price_average(products_price):
    total_price = sum(products_price.values())
    total_products = len(products_price)
    return total_price / total_products

# Create a new price list that reduces the old prices by $ 5
def reduce_prices_by_5(products_price):
    new_prices = {product: price - 5 for product, price in products_price.items()}
    return new_prices
# Calculate the total revenue generated from the products
def total_revenue(products_price, customer_purchases):
    revenue = 0
    for product, quantity in customer_purchases.items():
        price = products_price.get(product, 0)  
        revenue += price * quantity  
    return revenue
# Calculate the average daily revenue generated from the products
def average_daily_revenue(products_price, customer_purchases, num_days):
    total_revenue_value = total_revenue(products_price, customer_purchases)
    return total_revenue_value / 7
# Based on the new prices, which products are less than $ 30 
def products_less_than_30(new_prices):
    return [product for product, price in new_prices.items() if price <= 30]


# CALCULATOR PROMPT SECTION

is_on = True
while is_on:
    operation = input("Chose operation: \n A= Calculate total average price, \n B= create a new price list that reduces the old prices by $ 5\n C= calculate the total revenue generated from the products, \n D= calculate the average daily revenue generated from the products, \n E= based on the new prices, which products are less than $ 30,\n F= Switch off program? type 'off'").upper()
    if operation == "A":
        print("Total price average for all products:", total_price_average(products_price))
    elif operation== "B":
        new_prices = reduce_prices_by_5(products_price)
        print("New prices:", new_prices)

    elif operation == "C":
        print("Total revenue generated:", total_revenue(products_price, customer_purchases))

    elif operation == "D":
        print("Average daily revenue generated:", average_daily_revenue(products_price, customer_purchases, 1))
    elif operation == "E":
        products_less_than_30_list = products_less_than_30(products_price)
        print("Products less than $30:", products_less_than_30_list)
    elif operation == "OFF":
        is_on= False
    else:
        print("Enter a valid response")
        is_on= True

