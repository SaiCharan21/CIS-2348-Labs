# Name: Sai Todupunoori
# PSID: 2048092

def fullroster():
    keys = list(roster.keys())
    keys.sort()
    print("ROSTER")
    for x in keys:
        print("Jersey number: {}, Rating: {}".format(x, roster[x]))
    print("")


roster = dict()
cond = True
for x in range(0, 5):
    jersye = int(input("Enter player {}'s jersey number:\n".format(x + 1)))
    roster[jersye] = int(input("Enter player {}'s rating:\n".format(x + 1)))
    print("")

fullroster()

while cond:
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("")
    select = input("Choose an option:\n")

    if select == 'o':
        fullroster()

    elif select == 'd':
        jersey = int(input("Enter a player's jersey number: \n"))
        del roster[jersey]

    elif select == 'a':
        jersey = int(input("Enter a new player's jersey number: \n"))
        playerrating = int(input("Enter the player's rating:\n"))
        roster[jersey] = playerrating

    elif select == 'u':
        jersey = int(input("Enter a new player's jersey number: \n"))
        playerrating = int(input("Enter the player's rating:\n"))
        roster[jersey] = playerrating

    elif select == 'r':
        playerrating = int(input("Enter a rating:\n"))
        keys_list = list(roster.keys())
        keys_list.sort()
        print("ABOVE {}".format(playerrating))

        ct=0
        for i in keys_list:
            index = roster[i]
            if playerrating < index:
                print("Jersey number: {}, Rating: {}".format(i, index))
                ct += 1

        print("No players found above {} rating".format(playerrating)) if ct == 0 else None

    if select == "q":
        break
