# Product prices dictionary
product_prices = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules dictionary
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

# Function to calculate the discount based on rules
def calculate_discount(cart_total, quantity_dict):
    discount_applied = None
    discount_amount = 0

    if cart_total > 200:
        discount_applied = "flat_10_discount"
        discount_amount = 10
    elif any(quantity > 10 for quantity in quantity_dict.values()):
        discount_applied = "bulk_5_discount"
        discount_amount = 5
    elif sum(quantity_dict.values()) > 20:
        discount_applied = "bulk_10_discount"
        discount_amount = 10
    elif sum(quantity_dict.values()) > 30 and any(quantity > 15 for quantity in quantity_dict.values()):
        discount_applied = "tiered_50_discount"
        discount_amount = 50

    return discount_applied, discount_amount

# Function to calculate the total cost
def calculate_total(quantity_dict, discount_amount):
    subtotal = 0
    for product, quantity in quantity_dict.items():
        subtotal += product_prices[product] * quantity

    discount = (subtotal * discount_amount) / 100
    subtotal -= discount

    shipping_fee = 5 * ((sum(quantity_dict.values()) - 1) // 10 + 1)
    gift_wrap_fee = sum(quantity_dict.values())

    total = subtotal + shipping_fee + gift_wrap_fee

    return subtotal, discount, shipping_fee, gift_wrap_fee, total

# Main program
quantity_dict = {}

for product in product_prices:
    quantity = int(input(f"Enter the quantity of {product}: "))
    quantity_dict[product] = quantity

    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")
    if gift_wrap.lower() == "yes":
        gift_wrap_fee = quantity
    else:
        gift_wrap_fee = 0

subtotal, discount_amount = calculate_discount(sum(quantity_dict.values()), quantity_dict)
subtotal, discount, shipping_fee, gift_wrap_fee, total = calculate_total(quantity_dict, discount_amount)

# Output
print("Product Details:")
for product, quantity in quantity_dict.items():
    print(f"{product}: {quantity} - ${product_prices[product] * quantity}")

print(f"\nSubtotal: ${subtotal}")
print(f"Discount Applied: {discount_amount}% off ({discount})")

print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")

print(f"\nTotal: ${total}")