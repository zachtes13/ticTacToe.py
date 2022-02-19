from random import randint

#checkwin: function checks if a player has won
def checkwin(gb):
    #Column win
    if (gb[0][0] == "X" and gb[1][0] == "X" and gb[2][0] == "X") or (gb[0][1] == "X" and gb[1][1] == "X" and gb[2][1] == "X") or (gb[0][2] == "X" and gb[1][2] == "X" and gb[2][2] == "X"):
        print("X has won the game.")
        return True
    elif (gb[0][0] == "O" and gb[1][0] == "O" and gb[2][0] == "O") or (gb[0][1] == "O" and gb[1][1] == "O" and gb[2][1] == "O") or (gb[0][2] == "O" and gb[1][2] == "O" and gb[2][2] == "O"):
        print("O has won the game.")
        return True

    #Row win
    if (gb[0][0] == "X" and gb[0][1] == "X" and gb[0][2] == "X") or (gb[1][0] == "X" and gb[1][1] == "X" and gb[1][2] == "X") or (gb[2][0] == "X" and gb[2][1] == "X" and gb[2][2] == "X"):
        print("X has won the game.")
        return True
    elif (gb[0][0] == "O" and gb[0][1] == "O" and gb[0][2] == "O") or (gb[1][0] == "O" and gb[1][1] == "O" and gb[1][2] == "O") or (gb[2][0] == "O" and gb[2][1] == "O" and gb[2][2] == "O"):
        print("O has won the game.")
        return True

    #Diagonal win
    if (gb[0][0] == "X" and gb[1][1] == "X" and gb[2][2] == "X") or (gb[2][0] == "X" and gb[1][1] == "X" and gb[0][2] == "X"):
        print("X has won the game.")  
        return True
    elif (gb[0][0] == "O" and gb[1][1] == "O" and gb[2][2] == "O") or (gb[2][0] == "O" and gb[1][1] == "O" and gb[0][2] == "O"):
        print("O has won the game.")
        return True

#isgameover: function checks if game is over
def isgameover(gb):
    flag = True
    
    for row in range(0, 3):
        for col in range(0, 3):
            if gb[row][col] == " ":
                flag = False
                
    if checkwin(gb) == True:
        flag = True
    
    return flag

#printboard: function prints the game board in the correct format
def printboard(gb):
    print("\n")
    print(" " + gb[0][0] + " | " + gb[0][1] + " | " + gb[0][2])
    print("-----------")
    print(" " + gb[1][0] + " | " + gb[1][1] + " | " + gb[1][2])
    print("-----------")
    print(" " + gb[2][0] + " | " + gb[2][1] + " | " + gb[2][2])
    print("\n")

#resetboard: function resets the game board to default
def resetboard():
        
    print("  " + " | " + " " + " | " + " ")
    print("-----------")
    print("  " + " | " + " " + " | " + " ")
    print("-----------")
    print("  " + " | " + " " + " | " + " ") 
    print("\n")

#main function
gb = [[" "," "," "], [" "," "," "], [" "," "," "]]
players = {1 : "X", 2 : "O"}

print("""'Tic-Tac Toe' - random player starts. Enter moves as follows:

 tl | tc | tr
-------------
 ml | mc | mr
-------------
 bl | bc | br
""")

resetboard()

playerstart = randint(1, 2) 
print(str(players[playerstart]) + " starts.") 

currplayer = playerstart

currmove = input(str(players[currplayer]) + "'s turn: ")

while isgameover(gb) == False:
    falseinput = True
    while falseinput == True:
        if currmove.lower() == "tl" and gb[0][0] == " ":
            gb[0][0] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "tc" and gb[0][1] == " ":
            gb[0][1] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "tr" and gb[0][2] == " ":
            gb[0][2] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "ml" and gb[1][0] == " ":
            gb[1][0] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "mc" and gb[1][1] == " ":
            gb[1][1] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "mr" and gb[1][2] == " ":
            gb[1][2] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "bl" and gb[2][0] == " ":
            gb[2][0] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "bc" and gb[2][1] == " ":
            gb[2][1] = players[currplayer]
            falseinput = False
        elif currmove.lower() == "br" and gb[2][2] == " ":
            gb[2][2] = players[currplayer]
            falseinput = False
        else:
            currmove = input("Please enter a valid move: ")
    
    printboard(gb)
    
    if checkwin(gb) == True:
        break
    
    if isgameover(gb) == True:
        print("Cat's game!")
        break
    
    if currplayer == 1:
        currplayer = 2
    elif currplayer == 2:
        currplayer = 1
        
    currmove = input(str(players[currplayer]) + "'s turn: ")


