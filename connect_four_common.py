import connectfour
from collections import namedtuple
commandcombination=namedtuple('commandcombination',['order','colnum'])
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

def checkorder()->str:
    '''check if the order (which can be drop or pop) is valid, if valid, we return the sorted order'''
    while True:                
        try:
            originalcommand=input("Enter your move(for example, 'DROP column#' or 'POP column#'): ")
            commandlist=originalcommand.split()
            order=commandlist[0]
            colnum=int(commandlist[1])
            if order=='POP' or order=='DROP':
                return commandcombination(order,colnum)
        except:
            
            print("Input format error (must be 'DROP column#' or 'POP column#')")


























                        
    
    
