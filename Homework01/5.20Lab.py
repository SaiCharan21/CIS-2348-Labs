# Sai Charan Todupunoori
# PSID: 2048092

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")
print()
print("Davy's auto shop invoice")
print()
counter = 1
total_cost = 0
for car_service in (first_service, second_service):
    if car_service == 'Car wash':
        total_cost += 7
        print("Service {}: Car wash, $7".format(counter))
    elif car_service == '-':
        print("Service {}: No service".format(counter))
    elif car_service == 'Car wax':
        total_cost += 12
        print("Service {}: Car wax, $12".format(counter))
    elif car_service == 'Tire rotation':
        total_cost += 19
        print("Service {}: Tire rotation, $19".format(counter))
    elif car_service == 'Oil change':
        total_cost += 35
        print("Service {}: Oil change, $35".format(counter))
    counter = counter + 1
print()
print("Total: ${}".format(total_cost))
