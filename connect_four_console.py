import connectfour

def mainsingle():
    """this is the main function frame that operate in the single player status"""
    ConnectFourGameState=connectfour.new_game_state()
    print('Game start!\n')
    printboard(ConnectFourGameState)
    print("Enter your move(for example, 'DROP column#' or 'POP column#'\n")
    while True:
        #check if there is a winner
        winnernum=connectfour.winning_player(ConnectFourGameState)
        if winnernum== connectfour.NONE:
            if not checkboard(ConnectFourGameState):
                while True:
                    if ConnectFourGameState[1]==int(1):
                        print("Red turn.")
                    elif ConnectFourGameState[1]==int(2):
                        print("Yellow turn.")
                    try:
                        originalcommand=input("Enter your move: ")
                        order,colnum=command(originalcommand)
                        if (order=='POP' or order=='pop') or (order=='DROP' or order=='drop'):
                            break
                        else:
                            print("\nInput format error (must be 'DROP column#' or 'POP column#')\n")
                            
                    except:
                        print("\nInput format error (must be 'DROP column#' or 'POP column#')\n")
                if order=='DROP' or order=='drop':
                    try:
                        ConnectFourGameState=connectfour.drop_piece(ConnectFourGameState, colnum-1)
                    except connectfour.InvalidMoveError:
                        print('\nSorry, this column is already full\n')
                        
                if order=='POP' or order=='pop':
                    try:
                        ConnectFourGameState=connectfour.pop_piece(ConnectFourGameState, colnum-1)
                    except connectfour.InvalidMoveError:
                        print('\nSorry, this column is empty\n')
                printboard(ConnectFourGameState)
            else:
                print('\nThe board is already full, no winner.\n')
                return
        else:
            break
    printwinner(winnernum)
def command(command: str)->"order, column number":
    commandlist=command.split()
    order=commandlist[0]
    colnum=int(commandlist[1])
    return order, int(colnum)
def printboard(ConnectFourGameState):
    """print the board of the current state"""
    for colnum in range(connectfour.BOARD_COLUMNS):
        print(colnum+1, end='  ')
    for rownum in range(connectfour.BOARD_ROWS):
            print('')
            for colnum in range(connectfour.BOARD_COLUMNS):
                if ConnectFourGameState.board[colnum][rownum]==0:                    
                    print('.  ',end='')
                elif ConnectFourGameState.board[colnum][rownum]==1:
                    print('R  ',end='')
                else:
                    print('Y  ',end='')
    print('')
    
def printwinner(winnernum):
    """translate the number of player to color it represents"""
    if winnernum==1:
        print('The game is over! The winner is', ' RED')
    else:
        print('The game is over! The winner is', ' YELLOW')
            
def checkboard(ConnectFourGameState):
    """check if the board is all full"""
    
    for onelist in ConnectFourGameState.board:
        if 0 in onelist:
            return False
        else:
            pass
        
            
    return True
            
            
            
mainsingle()
