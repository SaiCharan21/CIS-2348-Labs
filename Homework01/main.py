money = int(input("Enter the change in cents:"))
cents = money % 100
dollars = money // 100

centsQuarter = cents % 25
quarters = cents // 25

centsDime = centsQuarter % 10
dimes = centsQuarter // 10

centsNickels = centsDime % 5
nickels = centsDime // 5

centsPennies = centsNickels % 1
pennies = centsNickels // 1

print("Your change is :", dollars, "dollar,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies,
      "pennies.")

# print("Houston Texans Schedule")
# print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
# print("Week    Day      Date                     Team")
# print("Week  1 Monday   09/09 at   New Orleans Saints\nWeek  2 Sunday   09/15 vs Jacksonville Jaguars\nWeek  3 Sunday   09/22 at   San Diego Chargers\nWeek  4 Sunday   09/29 vs    Carolina Panthers\nWeek  5 Sunday   10/06 vs      Atlanta Falcons")
# print("Week  6 Sunday   10/13 at   Kansas City Chiefs\nWeek  7 Sunday   10/20 at   Indianapolis Colts\nWeek  8 Sunday   10/27 vs      Oakland Raiders\nWeek  9 Sunday   11/03 at Jacksonville Jaguars\nWeek 10                                    Bye")
# print("Week 11 Sunday   11/17 at     Baltimore Ravens\nWeek 12 Thursday 11/21 vs   Indianapolis Colts\nWeek 13 Sunday   12/01 vs New England Patriots\nWeek 14 Sunday   12/08 vs       Denver Broncos")
# print("Week 15 Sunday   12/15 at     Tennessee Titans\nWeek 16 Sunday   12/22 at Tampa Bay Buccaneers\nWeek 17 Sunday   12/29 vs     Tennessee Titans")