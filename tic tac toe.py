#import magic
import random
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
def printBoard(board):
    for row in board:
        print (row)

players = input("Do you want to play with 1 or 2 people?")
if players=="2":
    printBoard(board)
    while True:
        row = int(input("Choose a row from 0 to 2\n"))
        col = int(input("Choose a column from 0 to 2\n"))
        while board[row][col]!="_":
            print("This is being occupied by a X or a O. Try again!")
            row = int(input("Choose a row from 0 to 2\n"))
            col = int(input("Choose a column from 0 to 2\n"))
        board[row][col]="X"
        printBoard(board)
        if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
            print("X wins!")
            break
        if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
            print("X wins!")
            break
        if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
            print("X wins!")
            break
        if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
            print("X wins!")
            break
        if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
            print("X wins!")
            break
        if board[0][0]!="_" and board[0][1]!="_" and board[0][2]!="_" and board[1][0]!="_" and board[1][1]!="_" and board[1][2]!="_" and board[2][0]!="_" and board[2][1]!="_" and board[2][2]!="_":
            print("It's a Draw!")
            break
        row = int(input("Choose a row from 0 to 2\n"))
        col = int(input("Choose a column from 0 to 2\n"))
        while board[row][col]!="_":
            print("This is being occupied by a X or a O. Try again!")
            row = int(input("Choose a row from 0 to 2\n"))
            col = int(input("Choose a column from 0 to 2\n"))
        board[row][col]="O"
        printBoard(board)
        if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
            print("O wins!")
            break
        if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
            print("O wins!")
            break
        if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
            print("O wins!")
            break
        if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
            print("O wins!")
            break
        if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
            print("O wins!")
            break
else:
    printBoard(board)
    while True:
        row = int(input("Choose a row from 0 to 2\n"))
        col = int(input("Choose a column from 0 to 2\n"))
        while board[row][col]!="_":
            print("This is being occupied by a X or a O. Try again!")
            row = int(input("Choose a row from 0 to 2\n"))
            col = int(input("Choose a column from 0 to 2\n"))
        board[row][col]="X"
        printBoard(board)
        if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
            print("X wins!")
            break
        if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
            print("X wins!")
            break
        if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
            print("X wins!")
            break
        if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
            print("X wins!")
            break
        if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
            print("X wins!")
            break
        if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
            print("X wins!")
            break
        if board[0][0]!="_" and board[0][1]!="_" and board[0][2]!="_" and board[1][0]!="_" and board[1][1]!="_" and board[1][2]!="_" and board[2][0]!="_" and board[2][1]!="_" and board[2][2]!="_":
            print("It's a Draw!")
            break
        print("AI's turn")
        row = random.randint(0,2)
        col = random.randint(0,2)
        while board[row][col]!="_":
            row = random.randint(0,2)
            col = random.randint(0,2)
        board[row][col]="O"
        printBoard(board)
        if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
            print("O wins!")
            break
        if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
            print("O wins!")
            break
        if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
            print("O wins!")
            break
        if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
            print("O wins!")
            break
        if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
            print("O wins!")
            break
        if board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
            print("O wins!")
            break


