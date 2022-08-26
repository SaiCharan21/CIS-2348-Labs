# Sai Charan Todupunoori
# PSID: 2048092
import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = height * width
print("Wall area:", area, "square feet")
paint_needed = area / 350
print("Paint needed:", '{:.2f}'.format(paint_needed), "gallons")
cans = int(math.ceil(paint_needed))
print("Cans needed: {} can(s)".format(cans))

print()

paint_color = input("Choose a color to paint the wall:\n")
color_costs = {'red': 35, 'green': 23, 'blue': 25}

if paint_color in color_costs:
    color_cost = color_costs.get(paint_color)
    total = color_costs[paint_color] * cans
    print("Cost of purchasing {} paint: ${}".format(paint_color, total))
