# Sai Charan Todupunoori
# PSID: 2048092

import csv

file_name = input()

word_list = []

with open(str(file_name), 'r') as csvfile:
    user_file = csv.reader(csvfile, delimiter=',')

    for row in user_file:
        for index in range(len(row)):
            if row[index] not in word_list:
                print(f'{row[index]} {row.count(row[index])}')
                word_list.append(row[index])
