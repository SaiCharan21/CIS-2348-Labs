# Sai Charan Todupunoori
# PSID: 2048092

import csv
from datetime import datetime, date


def PSD():
    # reading and adding each line/row in to the list records1
    records1 = []
    # this line is to assosciate each ID with each item in the manufacturer's list
    manu_id_col = []
    with open('ManufacturerList.csv', 'r') as manuf_file:
        for line in manuf_file:
            manu_id_col.append(
                line.split(',')[0])  # grabbing individual data to be used later in the writing to file function
            records1.append(line.split(','))

    # reading and adding each line/row in to the list records2
    records2 = []
    index_pos = 0
    with open('ServiceDatesList.csv', 'r') as service_file:
        for line in service_file:
            # comparing the current date vs service date in the csv file
            if (records2 == []) or (datetime.strptime(line.split(',')[1].strip(), "%m/%d/%Y") < datetime.strptime(
                    records2[len(records2) - 1][1].strip(), "%m/%d/%Y")):
                # adding the items that are past the service date on the day the program is actually executed
                records2.insert(index_pos, line.split(','))
            else:
                records2.insert(len(records2) + 1, line.split(','))

    # reading and adding each line/row in to the list records3
    records3 = []
    # this line is to assosciate each ID with each price
    price_id_col = []
    with open('PriceList.csv', 'r') as price_file:
        for line in price_file:
            price_id_col.append(
                line.split(',')[0])
            records3.append(line.split(','))

    # opening and creating the file
    with open('PastServiceDateInventory.csv', mode='w') as DamagedInventory_file:
        data = csv.writer(DamagedInventory_file, delimiter=',')
        for (service_itemID, service_date) in records2:
            # looping through records1  for service_itemID, service_date
            if records1[manu_id_col.index(service_itemID)][3]:
                # checking if item is damaged

                # writing data row based on using service item ID and service_date as a key value to access all the
                # contents of each list(records1,records2,records3) are being accessed based on their row index
                data.writerow([service_itemID, records1[manu_id_col.index(service_itemID)][1],
                               records1[manu_id_col.index(service_itemID)][2],
                               records3[price_id_col.index(service_itemID)][1].strip(), service_date.strip(),
                               records1[manu_id_col.index(service_itemID)][3].strip()])


if __name__ == '__main__':
    PSD()
