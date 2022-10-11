# Sai Charan Todupunoori
# PSID: 2048092

import datetime

inputDates = open('inputDates.txt', 'r')

parsedDates = open('parsedDates.txt', 'w')

months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
          "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}

current_date = datetime.datetime.now().date()

for line in inputDates:
    comma_index = line.find(",")

    if comma_index > 0:
        year = line[comma_index + 1:].strip()
        print(year)
        date = line[:comma_index]
        print(date)
        month = line[:date.find(" ")].strip().lower()
        print(month)
        day = date[date.find(" "):].strip()
        print(day)

        month_val = months[month]
        print(month_val)

        # converts basic date format to military time format to compare to current date in datetime library usage
        obj = datetime.datetime.strptime(str(month_val) + "/" + str(day) + "/" + str(year), '%m/%d/%Y')
        new_date = obj.date()
        print(obj)

        # creates the modified date format that is to be printed in the new txt file as output from input dates
        formatted_date = str(month_val) + "/" + str(day) + "/" + str(year)
        print(formatted_date)

        if current_date >= new_date:
            parsedDates.write(formatted_date)
            parsedDates.write('\n')

parsedDates.close()
inputDates.close()
