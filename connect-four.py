numberOfPlayers = 2
doneornot = 0

import random

def printBoard():
    global board
    b = ""
    for i in board:
        b += "|"
        for o in i:
            if o == 1: b += "⬛"
            elif o == 2: b += "⬜"
            else: b += "  "
        b += "|\n"
    b += "| 1 2 3 4 5 6 7|\n----------------"
    print(b)

def placeTile(team, column):
    global board
    column -= 1
    for i in range(6):
        if board[5 - i][column] == 0:
            board[5 - i][column] = team
            return True
    return False

def checkForZeros(fullboard):
    q = 0
    for i in range(6):
        q += fullboard[i].count(0)
    return q

def checkForWinComp(team):
    for i in range(6):
        for o in range(4):
            if board[i][o] == board[i][o + 1] == board[i][o + 2] == board[i][o + 3] == team: return True
    for i in range(3):
        for o in range(7):
            if board[i][o] == board[i + 1][o] == board[i + 2][o] == board[i + 3][o] == team: return True
    for i in range(3):
        for o in range(4):
            if board[i][o] == board[i + 1][o + 1] == board[i + 2][o + 2] == board[i + 3][o + 3] == team: return True
            if board[i + 3][o] == board[i + 2][o + 1] == board[i + 1][o + 2] == board[i][o + 3] == team: return True

while not doneornot:
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]


    p1name = input("Enter player 1's Name: ")
    if numberOfPlayers - 1: p2name = input("Enter player 2's Name: ")
    else: p2name = "Computer"

    winner = 0
    while True:
        inp = False
        printBoard()
        while not inp:
            try:
                Inp = int(input(p1name + "'s turn!\nInput a number and press enter."))
                inp = placeTile(1, Inp)
            except:
                print("Bad input, please input a number between 1 and 7.")
        if checkForWinComp(1):
            winner = 1
            break
        if checkForZeros(board) == 0:
            break
        if numberOfPlayers - 1:
            inp = False
            printBoard()
            while not inp:
                try:
                    Inp = int(input(p2name + "'s turn!\nInput a number and press enter."))
                    inp = placeTile(2, Inp)
                except:
                    print("Bad input, please input a number between 1 and 7.")
            if checkForWinComp(2):
                winner = 2
                break
            if checkForZeros(board) == 0:
                break
        else:
            inp = False
            while not inp:
                compguess = random.randint(1, 7)
                inp = placeTile(2, compguess)
            print("The computer went in column " + str(compguess))
            if checkForWinComp(2):
                winner = 2
                break
            if checkForZeros(board) == 1:
                break
            
    printBoard()
    if not winner:
        print("Tie!")
    else:
        if winner == 1:
            print(p1name + " wins!")
        else:
            print(p2name + " wins!")
    doneornot = input("Press enter to play again, or type something to quit.")