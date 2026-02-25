#In this lab you will write a function that calculates the final price of an item after applying a percentage discount.
#For example, if the price of an item is 50 and a discount of 20 is applied, the discount amount is 10, and the final price is 40.

#! Project 2: Discount Calculator
# Helps reinforce learning for conditional statements and logical operators

def applyDiscount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    elif not isinstance(discount, (int, float)):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        discountAmt = price * (discount / 100)
        finalPrice = price - discountAmt
        
    return finalPrice

print(applyDiscount(100,20))
print(applyDiscount(200, 50))
print(applyDiscount(50, 0))
print(applyDiscount(100, 100))
print(applyDiscount(74.5, 20.0))
