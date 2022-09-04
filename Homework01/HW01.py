# Sai Charan Todupunoori
# PSID: 2048092
print("      -------------------------")
print("         Birthday Calculator")
print("-----------------------------------------")

print("Current Date")

c_month = int(input("Please input the current month:\n"))
c_day = int(input("Please input the current day:\n"))
c_year = int(input("Please input the current year:\n"))

print("----------------------------------------")

print("Birthday Date")

bday_month = int(input("Please input the birthday month:\n"))
bday_day = int(input("Please input the birthday day:\n"))
bday_year = int(input("Please input the birthday year:\n"))

print("----------------------------------------")

age = c_year - bday_year

if (bday_month, bday_day) == (c_month, c_day):
    print("Happy Birthday!\nYou are {} years old!".format(age))
if c_month > bday_month:
    print(age)
elif (c_month == bday_month) and (bday_day < c_day):
    print("You are {} years old!".format(age))
elif c_month < bday_month:
    age -= 1
    print("You are {} years old!".format(age))
elif (c_month == bday_month) and (bday_day > c_day):
    age -= 1
    print("You are {} years old!".format(age))

