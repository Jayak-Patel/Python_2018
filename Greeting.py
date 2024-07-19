'''
stuff = ["ghost", "block", "pac-man"]
print(stuff[0])
print(stuff[1])
addstuff = input("What do you want to add?")
stuff.append(addstuff)
print(stuff)
print("Hello!")
name = input("What is your name?")
print("Nice to meet you",name+"!")
'''
grid = ["_","_","_"]
row=0
col=0
GameWin = True
while GameWin:
    print("Welcome to Tic-Tac-Toe!")
    row = input("Choose a row from 0 to 2")
    col = input("Choose a column from 0 to 2")
    if password==password1:
        print("Access Granted")
        question = input("Do you want to change the password?")
        if question=="yes" or question=="yeah" or question=="Yes":
            password1 = input("What is the new password?")
        else:
            print("Ok")
    else:
        print("Access Denied")
    program1 = input("Do you want to continue?")
    if program1=="no" or program1=="nah" or program1=="No":
        GameWin = False
print("You won!")
