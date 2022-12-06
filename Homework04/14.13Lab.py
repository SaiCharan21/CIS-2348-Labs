# Sai Charan Todupunoori
# PSID: 2048092

def partition(strings, begin, end):
    pivot = strings[end]
    index = begin - 1
    for j in range(begin, end):
        if strings[j] <= pivot:
            index += 1
            strings[index], strings[j] = strings[j], strings[index]
    strings[index + 1], strings[end] = strings[end], strings[index + 1]
    return index + 1


def quicksort(strings, begin, end):
    if end > begin:
        piv = partition(strings, begin, end)
        quicksort(strings, begin, piv - 1)
        quicksort(strings, piv + 1, end)


def main():
    strings = []
    string = input()
    while string != "-1":
        strings.append(string)
        string = input()
    ind = len(strings) - 1
    quicksort(strings, 0, ind)
    ex2 = 2 * len(strings) - 1
    calls = int(ex2)
    print(calls)

    for string in strings:
        print(string)


main()
