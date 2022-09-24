def exact_change(user_total):
    dollars = user_total // 100
    user_total = user_total % 100

    quarters = user_total // 25
    user_total = user_total % 25

    dimes = user_total // 10
    user_total = user_total % 10

    nickels = user_total // 5
    user_total = user_total % 5

    pennies = user_total // 1
    user_total = user_total % 1
    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    cents = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(cents)
    if (num_dollars == 0) and (num_quarters == 0) and (num_dimes == 0) and (num_nickels == 0) and (num_pennies == 0):
        print("no change")
    if num_dollars == 1:
        print(num_dollars, "dollar")
    elif num_dollars > 1:
        print(num_dollars, "dollars")
    if num_quarters == 1:
        print(num_quarters, "quarter")
    elif num_quarters > 1:
        print(num_quarters, "quarters")
    if num_dimes == 1:
        print(num_dimes, "dime")
    elif num_dimes > 1:
        print(num_dimes, "dimes")
    if num_nickels == 1:
        print(num_nickels, "nickel")
    elif num_nickels > 1:
        print(num_nickels, "nickels")
    if num_pennies == 1:
        print(num_pennies, "penny")
    elif num_pennies > 1:
        print(num_pennies, "pennies")
