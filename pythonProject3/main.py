line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]

game=True

def show_the_board():
    print(line1)
    print(line2)
    print(line3)
    print("\n")

def player1_move():
    show_the_board()
    print("Player1's turn...")
    line_1=int(input("Pick a line:"))
    column1=int(input("Pick a column: "))
    if line_1==1:
        if column1==1:
            if line1[0]==" ":
                line1.pop(0)
                line1.insert(0, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==2:
            if line1[1]==" ":
                line1.pop(1)
                line1.insert(1, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==3:
            if line1[2]==" ":
                line1.pop(2)
                line1.insert(2, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        else:
            print("Wrong value.Try again!\n\n")
            player1_move()
    elif line_1==2:
        if column1==1:
            if line2[0]==" ":
                line2.pop(0)
                line2.insert(0, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==2:
            if line2[1]==" ":
                line2.pop(1)
                line2.insert(1, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==3:
            if line2[2]==" ":
                line2.pop(2)
                line2.insert(2, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        else:
            print("Wrong value.Try again!\n\n")
            player1_move()
    elif line_1==3:
        if column1==1:
            if line3[0]==" ":
                line3.pop(0)
                line3.insert(0, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==2:
            if line3[1]==" ":
                line3.pop(1)
                line3.insert(1, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        elif column1==3:
            if line3[2]==" ":
                line3.pop(2)
                line3.insert(2, "X")
            else:
                print("That block has been used.Try another one!\n\n")
                player1_move()
        else:
            print("Wrong value.Try again!\n\n")
            player1_move()
    else:
        print("Wrong value.Try again!\n\n")
        player1_move()

def player2_move():
    show_the_board()
    print("Player2's turn...")
    line_2=int(input("Pick a line:"))
    column2=int(input("Pick a column: "))
    if line_2==1:
        if column2==1:
            if line1[0]==" ":
                line1.pop(0)
                line1.insert(0, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==2:
            if line1[1]==" ":
                line1.pop(1)
                line1.insert(1, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==3:
            if line1[2]==" ":
                line1.pop(2)
                line1.insert(2, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        else:
            print("Wrong value.Try again!\n\n")
            player2_move()
    elif line_2==2:
        if column2==1:
            if line2[0]==" ":
                line2.pop(0)
                line2.insert(0, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==2:
            if line2[1]==" ":
                line2.pop(1)
                line2.insert(1, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==3:
            if line2[2]==" ":
                line2.pop(2)
                line2.insert(2, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        else:
            print("Wrong value.Try again!\n\n")
            player2_move()
    elif line_2==3:
        if column2==1:
            if line3[0]==" ":
                line3.pop(0)
                line3.insert(0, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==2:
            if line3[1]==" ":
                line3.pop(1)
                line3.insert(1, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        elif column2==3:
            if line3[2]==" ":
                line3.pop(2)
                line3.insert(2, "O")
            else:
                print("That block has been used.Try another one!\n\n")
                player2_move()
        else:
            print("Wrong value.Try again!\n\n")
            player2_move()
    else:
        print("Wrong value.Try again!\n\n")
        player2_move()

def test():
    global game

    if line1[0]=="X" and line2[0]=="X" and line3[0]=="X":
        game=False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[0]=="O" and line2[0]=="O" and line3[0]=="O":
        game=False
        print("Gameover.Winner is Player2.")
        show_the_board()
    elif line1[1]=="X" and line2[1]=="X" and line3[1]=="X":
        game=False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[1]=="O" and line2[1]=="O" and line3[1]=="O":
        game=False
        show_the_board()
        print("Gameover.Winner is Player2.")
    elif line1[2]=="X" and line2[2]=="X" and line3[2]=="X":
        game=False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[2]=="O" and line2[2]=="O" and line3[2]=="O":
        game=False
        show_the_board()
        print("Gameover.Winner is Player2.")

    elif line1[0]=="X" and line1[1]=="X" and line1[2]=="X":
        game = False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[0]=="O" and line1[1]=="O" and line1[2]=="O":
        game = False
        show_the_board()
        print("Gameover.Winner is Player2.")
    elif line2[0] == "X" and line2[1] == "X" and line2[2] == "X":
        game = False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line2[0] == "O" and line2[1] == "O" and line2[2] == "O":
        game = False
        show_the_board()
        print("Gameover.Winner is Player2.")
    elif line3[0] == "X" and line3[1] == "X" and line3[2] == "X":
        game = False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line3[0] == "O" and line3[1] == "O" and line3[2] == "O":
        game = False
        show_the_board()
        print("Gameover.Winner is Player2.")

    elif line1[0]=="X" and line2[1]=="X" and line3[2]=="X":
        game = False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[0] == "O" and line2[1] == "O" and line3[2] == "O":
        game = False
        show_the_board()
        print("Gameover.Winner is Player2.")
    elif line1[2]=="X" and line2[1]=="X" and line3[0]=="X":
        game = False
        show_the_board()
        print("Gameover.Winner is Player1.")
    elif line1[2] == "O" and line2[1] == "O" and line3[0] == "O":
        game = False
        show_the_board()
        print("Gameover.Winner is Player2.")
    elif line1[0]!=" " and line1[1]!=" " and line1[2]!=" " and line2[0]!=" " and line2[1]!=" " and line2[2]!=" " and line3[0]!=" " and line3[1]!=" " and line3[2]!=" ":
        game = False
        show_the_board()
        print("Gameover.DRAW!")

print("***********************************************")
print("         WELCOME TO MINI 'XOX' GAME            ")
print("***********************************************\n")

while game:
    player1_move()
    print("\n")
    test()
    if game:
        player2_move()
        print("\n")
        test()
    else:
        break











