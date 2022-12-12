# Sai Charan Todupunoori
# PSID: 2048092

import csv
from datetime import datetime


# start of full_inventory function
def FI():
    # reading and adding each line/row in to the list records1
    records1 = []
    with open('ManufacturerList.csv', 'r') as f:
        # with open('ManufacturerList.csv', 'r') as f:
        for line in f:
            records1.append(line.split(','))

    # sorting in alphabetical order
    records1.sort(key=sort_key)

    # reading and adding each line/row in to the list records2
    records2 = []
    with open('ServiceDatesList.csv', 'r') as f:
        # with open('ServiceDatesList.csv', 'r') as f:
        for line in f:
            records2.append(line.split(','))

    # reading and adding each line/row in to the list records3
    records3 = []
    with open('PriceList.csv', 'r') as f:
        # with open('PriceList.csv', 'r') as f:
        for line in f:
            records3.append(line.split(','))

    # opening and creating the file
    list1 = []

    with open('FullInventory.csv', mode='w', newline='') as FullInventory_file:
        data = csv.writer(FullInventory_file, delimiter=',')
        for (itemID, manufacturer_name, item_type, indicator) in records1:
            # gathering data from manufacturer's file
            for (service_itemID, service_date) in records2:
                # gathering data from service dates list file
                if itemID == service_itemID:
                    # matching service data to item id
                    for (price_itemID, item_price) in records3:
                        # gathering data from prices list file
                        if itemID == price_itemID:
                            # matching price data to item id
                            list1.append(
                                [itemID, manufacturer_name, item_type, item_price.strip(), service_date.strip(),
                                 indicator.strip()])  # indicator variable is for damaged or not damaged

        data.writerows(list1)  # writing data row


def sort_key(records1):
    return records1[1]


def QueryFunction():
    FullInventoryRecords_uncleaned = []
    # Below block of code reads the FullInventory file and store the records to the above list
    with open('FullInventory.csv', 'r') as f:
        for line in f:
            FullInventoryRecords_uncleaned.append(line.strip().split(','))

    # Below block of code removes additional spaces in the data.
    FullInventoryRecords = []
    for record in FullInventoryRecords_uncleaned:
        FullInventoryRecords.append([i.strip() for i in record])

    # creating the list of all manufacturers and items in the inventory for lookup
    list_of_manufacturers_in_inventory = [j.strip() for j in [i[1] for i in FullInventoryRecords]]
    list_of_items_in_inventory = [j.strip() for j in [i[2] for i in FullInventoryRecords]]

    # Removing the duplicates of item types and manufacturers
    list_of_manufacuters_items_in_inventory = set(list_of_manufacturers_in_inventory + list_of_items_in_inventory)

    # function to sort the records - Used in the sort method
    def myfunc_sort(record):
        return int(record[3])

    def myfunc_sort2(record):
        return int(record[6])

    # Below block of code to take the input from the user and look in the inventory iteratively.
    Flag = True
    while Flag:
        userinput = input("Please Enter the manufacturer and item name or (q) to Quit: ").split(" ")
        userinput_cleaned_list = []

        # To Break out of the While Loop
        if userinput[0].strip().lower() == 'q':
            break

        # To remove the additional words e.g: nice,amazing,excellent by searching each word in the list of
        # manufacturers and item types.
        for word in userinput:
            if word in list_of_manufacuters_items_in_inventory:
                userinput_cleaned_list.append(word)

        try:
            input_manufacturer = userinput_cleaned_list[0]  # extract manufacturer name
            input_item = userinput_cleaned_list[1]  # extract item type
            # Below statements check if item is present in the inventory
            if input_item in list_of_items_in_inventory:
                item_with_same_manufacturer = []
                item_with_different_manufacturer = []

                for record in FullInventoryRecords:
                    # Matching
                    if input_item == record[2] and input_manufacturer == record[1]:
                        item_with_same_manufacturer.append(record)
                    elif input_item == record[2] and input_manufacturer != record[1]:
                        item_with_different_manufacturer.append(record)

                todays_date = datetime.now()
                # Item with same manufacturer
                item_with_same_manufacturer_filtered = [record for record in item_with_same_manufacturer if
                                                        datetime.strptime(record[4], '%m/%d/%Y') > todays_date and
                                                        record[5] != 'damaged']
                # Item with different manufacturer
                item_with_different_manufacturer_filtered = [record for record in item_with_different_manufacturer if
                                                             datetime.strptime(record[4], '%m/%d/%Y') > todays_date and
                                                             record[5] != 'damaged']

                final_output_same_manufacturer = ""
                if len(item_with_same_manufacturer_filtered) > 0:
                    item_with_same_manufacturer_filtered.sort(reverse=True, key=myfunc_sort)

                    final_output_same_manufacturer = item_with_same_manufacturer_filtered[0]
                    print("Your item is: {},{},{},{}".format(final_output_same_manufacturer[0],
                                                             final_output_same_manufacturer[1],
                                                             final_output_same_manufacturer[2],
                                                             final_output_same_manufacturer[3]))
                else:
                    pass

                # Below code performs the main functionalities provided in the requirement.
                if len(item_with_different_manufacturer_filtered) > 0:
                    # item_with_different_manufacturer_filtered.sort(reverse=True,key=myfunc_sort)
                    item_with_different_manufacturer_filtered_sorted = []
                    # List to store different manufacturer filtered records
                    if final_output_same_manufacturer != "":
                        final_output_same_manufacturer_price = final_output_same_manufacturer[3]
                        for record in item_with_different_manufacturer_filtered:
                            abs_difference = abs(int(record[3]) - int(
                                final_output_same_manufacturer_price))  # Calculating the differences
                            record = record + [abs_difference]
                            # print(record)
                            item_with_different_manufacturer_filtered_sorted.append(record)
                        item_with_different_manufacturer_filtered_sorted.sort(key=myfunc_sort2)
                        final_output_different_manufacturer = item_with_different_manufacturer_filtered_sorted[0]
                        print("You may,also, consider: {},{},{},{}".format(final_output_different_manufacturer[0],
                                                                           final_output_different_manufacturer[1],
                                                                           final_output_different_manufacturer[2],
                                                                           final_output_different_manufacturer[3]))
                    else:

                        print("Item not found")
                        item_with_different_manufacturer_filtered.sort(key=myfunc_sort)
                        final_output_different_manufacturer = item_with_different_manufacturer_filtered[0]
                        print("You may,also, consider: {},{},{},{}".format(final_output_different_manufacturer[0],
                                                                           final_output_different_manufacturer[1],
                                                                           final_output_different_manufacturer[2],
                                                                           final_output_different_manufacturer[3]))

            elif (input_item not in list_of_items_in_inventory) or (
                    input_manufacturer not in list_of_manufacturers_in_inventory):
                print("No such item in inventory")
        # Exception because of Index Error when either of the manufacturer or item type is not found in the inventory.
        except IndexError:
            print("No such item in inventory")


if __name__ == '__main__':
    FI()
    QueryFunction()
