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
while True:
    move = input("Who moves First 'Player' or 'Computer': ")
    if move == 'Player' or move == 'Computer':
        break
    else:
        print("Enter a valid Choice")


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
comp_win = [[0, 1, 2], [1, 0, 2], [0, 2, 1]]


def usermark():
    mark = True
    while mark:
        user_mark = int(input("Enter position of Marker: "))
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
        if position[0] == user_ch and position [1]  == user_ch:
            comp_mark = 2
        elif position[1] == user_ch and position[2] == user_ch:
            comp_mark = 0
        elif position[0] == user_ch and position[2] == user_ch:
            comp_mark = 1
        elif position[3] == user_ch and position[4] == user_ch:
            comp_mark = 5
        elif position[4] == user_ch and position[5] == user_ch:
            comp_mark = 3
        elif position[3] == user_ch and position[5] == user_ch:
            comp_mark = 4
        elif position[6] == user_ch and position[8] == user_ch:
            comp_mark = 7
        elif position[6] == user_ch and position[7] == user_ch:
            comp_mark = 8
        elif position[7] == user_ch and position[8] == user_ch:
            comp_mark = 6
        elif position[0] == user_ch and position[3] == user_ch:
            comp_mark = 6
        elif position[0] == user_ch and position[6] == user_ch:
            comp_mark = 3
        elif position[3] == user_ch and position[6] == user_ch:
            comp_mark = 0
        elif position[1] == user_ch and position[4] == user_ch:
            comp_mark = 7
        elif position[4] == user_ch and position[7] == user_ch:
            comp_mark = 1
        elif position[1] == user_ch and position[7] == user_ch:
            comp_mark = 4
        elif position[6] == user_ch and position[3] == user_ch:
            comp_mark = 0
        elif position[2] == user_ch and position[5] == user_ch:
            comp_mark = 8
        elif position[5] == user_ch and position[8] == user_ch:
            comp_mark = 2
        elif position[2] == user_ch and position[8] == user_ch:
            comp_mark = 5
        elif position[0] == user_ch and position[4] == user_ch:
            comp_mark = 8
        elif position[0] == user_ch and position[8] == user_ch:
            comp_mark = 4
        elif position[4] == user_ch and position[8] == user_ch:
            comp_mark = 0
        elif position[6] == user_ch and position[4] == user_ch:
            comp_mark = 2
        elif position[6] == user_ch and position[2] == user_ch:
            comp_mark = 4
        elif position[2] == user_ch and position[4] == user_ch:
            comp_mark = 6
        #else:

        if comp_mark  not in occ_pos:
            occ_pos.append(comp_mark)
            position[comp_mark] = comp_ch
            mark = False
        else:
            comp_mark = random.randint(0, 8)
            if comp_mark in occ_pos:
                continue
            else:
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


#def comp_block(mark):




while len(occ_pos) < 9:
    if move == "Player":
        gameboard()
        usermark()
        if len(occ_pos) == 9:
            break
        else:
            compmark()
    elif move == "Computer":
        compmark()
        gameboard()
        if len(occ_pos) == 9:
            break
        else:
            usermark()
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
