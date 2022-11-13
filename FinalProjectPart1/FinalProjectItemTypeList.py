# Sai Charan Todupunoori
# PSID: 2048092

import csv


def ITL():
    records1 = []
    records2 = []
    records3 = []

    with open('ManufacturerList.csv', 'r') as manuf_file:
        for line in manuf_file:
            records1.append(line.split(','))
    records1.sort(key=sort_key)

    with open('ServiceDatesList.csv', 'r') as f:
        for line in f:
            records2.append(line.split(','))

    with open('PriceList.csv', 'r') as f:
        for line in f:
            records3.append(line.split(','))

    dict1 = {}
    for (itemID, manufacturer_name, item_type, indicator) in records1:
        for (service_itemID, service_date) in records2:
            if itemID == service_itemID:
                for (price_itemID, item_price) in records3:
                    if itemID == price_itemID and item_type in dict1.keys():
                        dict1[item_type].append([itemID, manufacturer_name, item_price.strip(),
                                                 service_date.strip(),
                                                 indicator.strip()])
                    elif itemID == price_itemID and item_type not in dict1.keys():
                        dict1[item_type] = list([[itemID, manufacturer_name, item_price.strip(),
                                                  service_date.strip(),
                                                  indicator.strip()]])

    for item_type in dict1:
        with open(item_type.capitalize() + 'Inventory.csv', mode='w', newline='') as item_type_file:
            data = csv.writer(item_type_file, delimiter=',')
            for item_data_list in dict1[item_type]:
                data.writerow(item_data_list)


def sort_key(records1):
    return records1[0]


# calling the function FI()
if __name__ == '__main__':
    ITL()
