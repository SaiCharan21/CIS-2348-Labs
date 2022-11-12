# Sai Charan Todupunoori
# PSID: 2048092

import csv


# start of full_inventory function
def FI():
    # reading and adding each line/row in to the list records1
    records1 = []
    with open('ManufacturerList.csv', 'r') as f:
        for line in f:
            records1.append(line.split(','))

    # sorting in alphabetical order
    records1.sort(key=sort_key)

    # reading and adding each line/row in to the list records2
    records2 = []
    with open('ServiceDatesList.csv', 'r') as f:
        for line in f:
            records2.append(line.split(','))

    # reading and adding each line/row in to the list records3
    records3 = []
    with open('PriceList.csv', 'r') as f:
        for line in f:
            records3.append(line.split(','))

    # opening and creating the file
    with open('FullInventory.csv', mode='w', newline='') as FullInventory_file:
        data = csv.writer(FullInventory_file, delimiter=',')
        for (itemID, manufacturer_name, item_type, indicator) in records1:
            # looping through records1  for itemID, manufacturer_name, item_type, damaged or not damaged condition
            for (service_itemID, service_date) in records2:
                # looping through records2  for service_itemID, service_date
                if itemID == service_itemID:
                    # matching the item id from full inventory file to service dates list file
                    for (price_itemID, item_price) in records3:
                        # looping through records3  for price_itemID, item_price
                        if itemID == price_itemID:
                            # matching the item id from full inventory file to prices list file
                            data.writerow(
                                [itemID, manufacturer_name, item_type, indicator.strip(), service_date.strip(),
                                 item_price.strip()])


# sorting function taking in manufacturers list element: manufacturer name
def sort_key(records1):
    return records1[1]


# calling the function FI()
if __name__ == '__main__':
    FI()
