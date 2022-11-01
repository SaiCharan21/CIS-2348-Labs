# Name: Sai Todupunoori
# PSID: 2048092

if __name__ == '__main__':
    string = input()
    list = [int(x) for x in string.split(" ") if int(x) >= 0]
    list.sort()
    [print(i, end=' ') for i in list]

