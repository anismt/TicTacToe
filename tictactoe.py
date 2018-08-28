def tictactoe(): 
    board = [1,2,3,4,5,6,7,8,9] 
    check = False 
    win_solutions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) 
    def drawboardlayout(): 
        print(board[0], board[1], board[2]) 
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
    def player1(): 
        x = int(raw_input("Player 1, place your X: ")) 
        x -= 1 
        if x not in range(0, 9) or board[x] == "X" or board[x] == "O": 
            print("Oops! There is either an x, or an o or that place does not exist on the grid. Please try again.") 
            player1() 
        else: 
            board[x] = "X" 
    def player2(): 
        o = int(raw_input("Player 2, place your O: ")) 
        o -= 1 
        if o not in range(0, 9) or board[o] == "X" or board[o] == "O":
            print("\nOops! There is either an x, or an o or that place does not exist on the grid. Please try again.")
            player2() 
        else:
            board[o] = "O" 
    def checking_board():
        count = 0
        for answer in win_solutions:            
            if board[answer[0]] == board[answer[1]] == board[answer[2]] == "X":
                print("Hooray! Player 1 wins! Congratulations!\n")
                return True          
            if board[answer[0]] == board[answer[1]] == board[answer[2]] == "O":
                print("Hooray! Player 2 Wins! Congratulations!\n")
                return True
        for tie in range(9):           
            if board[tie] == "X" or board[tie] == "O":
                count += 1           
            if count == 9:
                print ("It's a draw!\n")
                return True
    while not check:
        drawboardlayout()
        check = checking_board()
        if check == True:
            break
        player1()
        print
        drawboardlayout()
        check = checking_board()
        if check == True:
            break
        player2()
        print
    if raw_input("Do you want to play again (yes/no) ") == "yes": 
        tictactoe()
    else:
       quit() 
tictactoe()
    