import connect_four_common
import connect_four_socket
import connectfour
def _welcome_check()-> str:
    '''let the user input the username, server will check if it follows protocol'''    
    while True:
            mesgcheck=input()
            if mesgcheck.startswith('I32CFSP_HELLO ') and len(mesgcheck)>14:
                return mesgcheck
            else:
                print('Format error. Please input username after "I32CFSP_HELLO "')

def userinterface():
    '''This is the main user interface of the sever version'''
    try:
        Connectionfour=connect_four_socket.connect('woodhouse.ics.uci.edu',4444)
    #except doesn't work???
    #except connect_four_socket.ServerNoResponseError():
        #pass
    except:
        print('No response from server')
    ConnectFourGameState=startstatecheck(Connectionfour)
    while True:
        winnernum=connectfour.winning_player(ConnectFourGameState)
        if winnernum== connectfour.NONE:        
            if ConnectFourGameState.turn==1:
                '''This if statement handle client's move'''
                order,colnum=userinput()
                if order.upper()=='DROP':
                    try:
                        ConnectFourGameState=connectfour.drop_piece(ConnectFourGameState, colnum-1)
                    except connectfour.InvalidMoveError:
                        print('Sorry, this column is already full')                       
                if order.upper()=='POP':
                    try:
                        ConnectFourGameState=connectfour.pop_piece(ConnectFourGameState, colnum-1)
                    except connectfour.InvalidMoveError:
                        print('Sorry, this column is empty')
                connect_four_common.printboard(ConnectFourGameState)
            elif ConnectFourGameState.turn==2:
        
                '''This if statement handle server's move'''
                ConnectFourGameState=servermove(ConnectFourGameState,Connectionfour,order,colnum)
        else:
            return

def servermove(ConnectFourGameState,Connectionfour,order,colnum)->connectfour.ConnectFourGameState:
    '''send the order to server and return its reply'''
    connect_four_socket.write(Connectionfour,order+' '+str(colnum))
    connect_four_socket.checkOKAY(Connectionfour)
    reply=connect_four_socket.readline(Connectionfour).split()
    replyorder=reply[0]
    replycolnum=int(reply[1])
    print('The server decides to', reply[0],'at column',reply[1])
    if replyorder.upper()=='DROP':
        try:
            ConnectFourGameState=connectfour.drop_piece(ConnectFourGameState, replycolnum-1)
        except connectfour.InvalidMoveError:
            print('Sorry, this column is already full')                       
    if replyorder.upper()=='POP':
        try:
            ConnectFourGameState=connectfour.pop_piece(ConnectFourGameState, replycolnum-1)
        except connectfour.InvalidMoveError:
            print('Sorry, this column is empty')
    connect_four_socket.expect(Connectionfour,'READY')  
    connect_four_common.printboard(ConnectFourGameState)
    return ConnectFourGameState
    

def startstatecheck(Connectionfour)->connectfour.ConnectFourGameState:
    '''Handle all the start states protocol checking'''
    welcomemesg=_welcome_check()
    connect_four_socket.checkhello(Connectionfour,welcomemesg)
    connect_four_socket.checkAI(Connectionfour)
    ConnectFourGameState=connectfour.new_game_state()
    print('This is the gameboard:')
    connect_four_common.printboard(ConnectFourGameState)
    print('game start!')
    print('You are RED!')
    return ConnectFourGameState

def userinput()->str:
    '''Let user input order and check if it follow the protocol'''
    return connect_four_common.checkorder()
    

    



userinterface()
