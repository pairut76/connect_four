   
import connectfour

def mainsingle():#type in 'asfa' return error
    """this is the main function frame that operate in the single player status"""
    ConnectFourGameState=connectfour.new_game_state()
    print('Game start!\n')
    printboard(ConnectFourGameState)
    originalcommand=input("Enter your move(for example, 'DROP column#' or 'POP column#'): ")
    # instruct player only once about the input format
    # print board once at the beginning
    # print whose turn it is
    # ? ask user to drop and pop (dont change this one now, lets finish other parts first)
    # accept both capital and lower case
    while True:
        #check if there is a winner
        winnernum=connectfour.winning_player(ConnectFourGameState)
        if winnernum== connectfour.NONE:
            if not checkboard(ConnectFourGameState):
                while True:                
                    try:
                        originalcommand=input("Enter your move: ")
                        commandlist=originalcommand.split()
                        order=commandlist[0]
                        colnum=int(commandlist[1])
                        if (order=='POP') or (order=='DROP'):
                            break
                    except:
                        print("Input format error (must be 'DROP column#' or 'POP column#')")
                if order=='DROP':
                    try:
                        ConnectFourGameState=connectfour.drop_piece(ConnectFourGameState, colnum-1)
                    except (connectfour.InvalidMoveError):
                        print('Sorry, this column is already full')
                        
                if order=='POP':
                    try:
                        ConnectFourGameState=connectfour.pop_piece(ConnectFourGameState, colnum-1)
                        
                    except (connectfour.InvalidMoveError):
                        print('Sorry, this column is empty')
                printboard(ConnectFourGameState)
            else:
                print('The board is already full, no winner.')
                return
        else:
            break
    printwinner(winnernum)
                
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
    
