# Sai Charan Todupunoori
# PSID: 2048092

string = input().split()
while string[0] != '-1':
    try:
        p1 = int(string[1])
        ageVal = p1 + 1
    except ValueError:
        ageVal = 0
    print('{} {}'.format(string[0], ageVal))
    string = input().split()
    string[0]
