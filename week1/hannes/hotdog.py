import math


def ui_line():
    print("-" * 64)


ui_line()

try:
    two_hotdogs = int(input("How many want 2 hotdogs?\n> "))
    three_hotdogs = int(input("How many want 3 hotdogs?\n> "))
    two_vegan_hotdogs = int(input("How many want 2 vegan hotdogs?\n> "))
    three_vegan_hotdogs = int(input("How many want 3 vegan hotdogs?\n> "))
except ValueError:
    print("You must enter numbers!!!")
    exit(1)

ui_line()

drinks = two_hotdogs + three_hotdogs + two_vegan_hotdogs + three_vegan_hotdogs
drink_cost = round(drinks * 13.95, 2)

hotdogs = 2 * two_hotdogs + 3 * three_hotdogs
hotdogs_packages = math.ceil(hotdogs / 8)
hotdog_cost = round(hotdogs_packages * 20.95, 2)  # Round to 2 decimal places

vegan_hotdogs = 2 * two_vegan_hotdogs + 3 * three_vegan_hotdogs
vegan_hotdog_packages = math.ceil(vegan_hotdogs / 4)
vegan_hotdog_cost = round(vegan_hotdog_packages * 34.95, 2)

total_cost = round(drink_cost + hotdog_cost + vegan_hotdog_cost, 2)

table = [
    ["AMOUNT", "ITEM", "COST"],
    [hotdogs_packages, "HOTDOG PACKAGES", f"{hotdog_cost}:-"],
    [vegan_hotdog_packages, "VEGAN PACKAGES", f"{vegan_hotdog_cost}:-"],
    [drinks, "DRINKS", f"{drink_cost}:-"],
]

for row in table:
    print(f"{row[0]:<12} {row[1]:<24} {row[2]:<12}")  # :<(spacing) = left-align

ui_line()
print(f"Total cost: {total_cost}:-")
ui_line()
