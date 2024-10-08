import math
from decimal import (
    Decimal,
)  # idomatic way to handling decimal numbers in python without float

try:
    two_hotdogs = int(input("How many want 2 hotdogs? "))
    three_hotdogs = int(input("How many want 3 hotdogs? "))
    two_vegan_hotdogs = int(input("How many want 2 vegan hotdogs? "))
    three_vegan_hotdogs = int(input("How many want 3 vegan hotdogs? "))
except ValueError:
    print("You must enter numbers!!!")
    exit(1)

drinks = two_hotdogs + three_hotdogs + two_vegan_hotdogs + three_vegan_hotdogs
drink_cost = drinks * Decimal(
    "13.95"
)  # Use Decimal to avoid floating-point inaccuracies
print(f"DRINKS:\t{drink_cost}:-")

hotdogs = 2 * two_hotdogs + 3 * three_hotdogs
hotdog_cost = math.ceil(hotdogs / 8) * Decimal("20.95")
print(f"HOTDOG:\t{hotdog_cost}:-")

vegan_hotdogs = 2 * two_vegan_hotdogs + 3 * three_vegan_hotdogs
vegan_hotdog_cost = math.ceil(vegan_hotdogs / 4) * Decimal("34.95")

print(f"VEGAN:\t{vegan_hotdog_cost}:-")

total_cost = round(drink_cost + hotdog_cost + vegan_hotdog_cost, 2)
print(f"Total cost: {drink_cost + hotdog_cost + vegan_hotdog_cost}:-")
