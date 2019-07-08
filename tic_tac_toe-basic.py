import random

position = [0, 1, 2, 3, 4, 5, 6, 7, 8]
while True:
    choice = input("Enter Your Choice 'X' or '0': ")
    if choice == 'X' or choice == '0':
        break
    else:
        print("Enter a valid Choice")
if choice == "X":
    user_ch = "X"
    comp_ch = "0"

else:
    user_ch = "0"
    comp_ch = "X"


def gameboard():
    print("""
           {} | {} | {}
         ----------------
           {} | {} | {}
         ----------------
           {} | {} | {}

    """.format(position[0], position[1], position[2],
               position[3], position[4], position[5],
               position[6], position[7], position[8]))


occ_pos = []


def usermark():
    mark = True
    while mark:
        user_mark = int(input(("Enter position of Marker: ")))
        if user_mark in occ_pos:
            print("Position Already Occupied")
            continue
        elif user_mark > 8:
            print("Enter Valid Position")
        else:
            # print(user_mark)
            occ_pos.append(user_mark)
            position[user_mark] = user_ch
            mark = False


def compmark():
    mark = True
    while mark:
        comp_mark = random.randint(0, 8)
        if comp_mark in occ_pos:
            continue
        else:
            # print(comp_mark)
            occ_pos.append(comp_mark)
            position[comp_mark] = comp_ch
            mark = False


def win(mark, req_1, req_2, req_3):
    if position[req_1] == mark and position[req_2] == mark and position[req_3] == mark:
        return True


def condition(mark):
    if win(mark, 0, 1, 2):
        return True
    elif win(mark, 3, 4, 5):
        return True
    elif win(mark, 6, 7, 8):
        return True

    elif win(mark, 0, 3, 6):
        return True
    elif win(mark, 1, 4, 7):
        return True
    elif win(mark, 2, 5, 8):
        return True

    elif win(mark, 0, 4, 8):
        return True
    elif win(mark, 2, 4, 6):
        return True


while len(occ_pos) < 9:
    gameboard()
    usermark()
    if len(occ_pos) == 9:
        break
    else:
        compmark()
    if condition(user_ch) == True:
        gameboard()
        print("--------------------Win----------------------")
        break
    elif condition(comp_ch) == True:
        gameboard()
        print("--------------------Lose---------------------")
        break

if len(occ_pos) == 9:
    gameboard()
    print("-----------Game Draw----------------")

# print(occ_pos)
# print(user_ch,comp_ch)
