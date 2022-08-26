#Sai Charan Todupunoori
#PSID: 2048092

amt_lemon_juice = int(input("Enter amount of lemon juice (in cups):\n"))
amt_water = int(input("Enter amount of water (in cups):\n"))
amt_agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(amt_lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(amt_water), "cup(s) water")
print('{:.2f}'.format(amt_agave), "cup(s) agave nectar")
print()
amt_servings = int(input("How many servings would you like to make?\n"))
print()
amt_servings = amt_servings / servings
print("Lemonade ingredients - yields", '{:.2f}'.format(servings*amt_servings), "servings")
print('{:.2f}'.format(amt_lemon_juice*amt_servings), "cup(s) lemon juice")
print('{:.2f}'.format(amt_water*amt_servings), "cup(s) water")
print('{:.2f}'.format(amt_agave*amt_servings), "cup(s) agave nectar")
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(servings*amt_servings), "servings")
print('{:.2f}'.format((amt_lemon_juice*amt_servings)/16), "gallon(s) lemon juice")
print('{:.2f}'.format((amt_water*amt_servings)/16), "gallon(s) water")
print('{:.2f}'.format((amt_agave*amt_servings)/16), "gallon(s) agave nectar")





