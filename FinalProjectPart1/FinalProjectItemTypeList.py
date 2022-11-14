# Sai Charan Todupunoori
# PSID: 2048092

import csv


def ITL():
    # these are lists which will hold each CSVs data when reading each file
    records1 = []
    records2 = []
    records3 = []

    # reading and adding each line/row in to the list records1
    with open('ManufacturerList.csv', 'r') as manuf_file:
        for line in manuf_file:
            records1.append(line.split(','))
    # sorting in ID order
    records1.sort(key=sort_key)

    # reading and adding each line/row in to the list records2
    with open('ServiceDatesList.csv', 'r') as f:
        for line in f:
            records2.append(line.split(','))

    # reading and adding each line/row in to the list records3
    with open('PriceList.csv', 'r') as f:
        for line in f:
            records3.append(line.split(','))

    dict1 = {}
    for (itemID, manufacturer_name, item_type, indicator) in records1:
        # gathering data from manufacturer's file
        for (service_itemID, service_date) in records2:
            # gathering data from service dates file
            if itemID == service_itemID:  # matching service data to item id
                for (price_itemID, item_price) in records3:
                    # gathering data from prices list file
                    if itemID == price_itemID and item_type in dict1.keys():
                        # checking to make sure the products match up to each others ID and other attributes

                        # loops and adds matched products by item type to dict
                        dict1[item_type].append([itemID, manufacturer_name, item_price.strip(),
                                                 service_date.strip(),
                                                 indicator.strip()])

                    # this code is for when the item/product attributes do not match
                    elif itemID == price_itemID and item_type not in dict1.keys():
                        dict1[item_type] = list([[itemID, manufacturer_name, item_price.strip(),
                                                  service_date.strip(),
                                                  indicator.strip()]])

    # dynamically creating output files based on item type and adding row data as per item type
    for item_type in dict1:
        # opening the file connection for writing
        with open(item_type.capitalize() + 'Inventory.csv', mode='w', newline='') as item_type_file:
            # creating file writer
            data = csv.writer(item_type_file, delimiter=',')
            # writes each row in the dict based on whatver data was appended to dict1
            for i in dict1[item_type]:
                data.writerow(i)


def sort_key(records1):
    return records1[0]


# calling the function FI()
if __name__ == '__main__':
    ITL()
