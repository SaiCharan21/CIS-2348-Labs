# Sai Charan Todupunoori
# PSID: 2048092

import csv


# start of damaged inventory function
def DI():
    # reading and adding each line/row in to the list records1
    records1 = []
    with open('ManufacturerList.csv', 'r') as manuf_file:
        for line in manuf_file:
            records1.append(line.split(','))

    # reading and adding each line/row in to the list records2
    records2 = []
    service_id_col = []
    with open('ServiceDatesList.csv', 'r') as service_file:
        for line in service_file:
            service_id_col.append(
                line.split(',')[0])  # grabbing ID reference to be used later in the writing to file function
            records2.append(line.split(','))

    # reading and adding each line/row in to the list records3
    records3 = []
    price_id_col = []
    with open('PriceList.csv', 'r') as price_file:
        for line in price_file:
            price_id_col.append(
                line.split(',')[0])  # grabbing ID reference to be used later in the writing to file function
            records3.append(line.split(','))
    records3.sort(key=sort_key, reverse=True)

    # opening and creating the file
    with open('DamagedInventory.csv', mode='w', newline='') as DamagedInventory_file:
        data = csv.writer(DamagedInventory_file, delimiter=',')
        for (itemID, manufacturer_name, item_type, indicator) in records1:
            # looping through records1  for itemID, manufacturer_name, item_type, damaged or not damaged condition
            # checking if item is damaged
            if indicator.strip():
                # writing to new csv file taking the data of each list
                data.writerow([itemID, manufacturer_name, item_type, records3[price_id_col.index(itemID)][1].strip(),
                               records2[service_id_col.index(itemID)][1].strip()])


# sorting function taking in manufacturers list element: manufacturer name
def sort_key(records3):
    print(records3[1])
    return records3[1]


# calling the function FI()
if __name__ == '__main__':
    DI()
