import socket
from collections import namedtuple
Connectionfour=namedtuple('Connectionfour',['socket','input','output'])
def connect(host: str, port: int) -> Connectionfour:
    '''
    connect the specified server as specified by the user
    '''

    connectfour_socket = socket.socket()
    
    connectfour_socket.connect((host, port))

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')
    print('connected')
    return Connectionfour(
        socket = connectfour_socket,
        input = connectfour_input,
        output = connectfour_output)

class ServerNoResponseError(Exception):
    pass

class ServerError(Exception):# small problem in entering ICSSas as as
    pass

def checkhello(connection:Connectionfour,message:str)->None:
    '''Send the hello mesg and check if the received mesg is correct in format'''
    username=message[14:]
    write(connection,message)
    expect(connection,'WELCOME '+username)

def checkAI(connection:Connectionfour)->None:
    '''Send the AI_GAME mesg and check if the received mesg is correct in format'''
    AIinfo=input()
    write(connection,AIinfo)
    expect(connection,'READY')

def checkREADY(connection:Connectionfour)->None:
    '''Check if the server is ready'''
    expect(connection,'READY')

def write(connection:Connectionfour,message:str)->None:
    '''send the specified mesg out and expect the reply from the server'''
    
    connection.output.write(message+'\r\n')
    connection.output.flush()
    

def expect(connection:Connectionfour,expected:str)->None:
    '''check if the reply from the server has right format and if there is a winner'''
    mesg=readline(connection)
    print(mesg)
    if mesg[0:6]=="WINNER":
        close(connection)
        return
    
    if not mesg.startswith(expected):
        raise ServerError()
        
    

def readline(connection:Connectionfour)->str:
    '''read the line that returned from the server'''
    return connection.input.readline()[:-1]

def checkOKAY(connection:Connectionfour)->None:
    '''check if the reply from the server is OKAY or winner'''
    try:
        
        expect(connection,'OKAY')        
    except:
        readline(connection)        
        close(connection)

def close(connection:Connectionfour)->None:
    '''close all the connecitons'''
    connection.socket.close()
    connection.input.close()
    connection.output.close()
    
















