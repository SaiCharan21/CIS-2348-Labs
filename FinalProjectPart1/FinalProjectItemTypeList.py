# Sai Charan Todupunoori
# PSID: 2048092

import csv


# start of full_inventory function
def FI():
    # reading and adding each line/row in to the list records1
    records1 = []
    all_types = []
    # this line is to assosciate each ID with each item in the manufacturer's list
    manu_id_col = []
    with open('ManufacturerList.csv', 'r') as manuf_file:
        for line in manuf_file:
            manu_id_col.append(
                line.split(',')[0])  # grabbing individual data to be used later in the writing to file function

            types = line.split(',')[2]
            all_types.append(str(types))

            records1.append(line.split(','))
        print(all_types)

    # sorting in alphabetical order
    records1.sort(key=sort_id)

    # reading and adding each line/row in to the list records2
    records2 = []
    service_id_col = []
    with open('ServiceDatesList.csv', 'r') as service_file:
        for line in service_file:
            service_id_col.append(line.split(',')[0])
            records2.append(line.split(','))

    # reading and adding each line/row in to the list records3
    records3 = []
    price_id_col = []
    with open('PriceList.csv', 'r') as price_file:
        for line in price_file:
            price_id_col.append(line.split(',')[0])
            records3.append(line.split(','))

        # opening and creating the file
    for (service_itemID, service_date) in records2:
        typeName = records1[manu_id_col.index(service_itemID)][2].capitalize()
        for item in all_types:
            file = open(typeName + "Inventory.csv", "w")

            new_data = csv.writer(file, delimiter=',')
            if typeName == item:
                new_data.writerow([service_itemID, records1[manu_id_col.index(service_itemID)][1],
                                   records1[manu_id_col.index(service_itemID)][2],
                                   records3[price_id_col.index(service_itemID)][1].strip(), service_date.strip(),
                                   records1[manu_id_col.index(service_itemID)][3].strip()])


# sorting function taking in manufacturers list element: manufacturer name
def sort_key(records1):
    return records1[1]


def sort_id(records1):
    return records1[0]


# calling the function FI()
if __name__ == '__main__':
    FI()
