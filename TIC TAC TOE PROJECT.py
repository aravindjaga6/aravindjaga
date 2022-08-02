


def display_board(board):


    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("   |   | ")
    print(' ---------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("   |   | ")
    print(' ---------')
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    
    marker = ''
    
    while not marker == 'X' or marker == 'O':
        
        marker = input("Player 1, Do you want to be a X or O : ").upper()
        
        if marker == 'X':
            return ('X', 'O')  #tuple unpack method
        else:
            return ('O', 'X')


def place_marker(board, marker, position):
    
    board[position] = marker




def win_check(board, marker):
    
    return ((board[3] == marker and board[5] == marker and board[7] == marker) or
    (board[1] == marker and board[2] == marker and board[3] == marker) or
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker) or
    (board[1] == marker and board[5] == marker and board[9] == marker))



import random

def first_turn():

    flip = random.randint(0, 1)

    if flip == 0:
        return 'player 2'
    else:
        return 'player 1'




def space_check(board, position):
    
    return board[position] == ' '
    



def fullboard_check(board):
    
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    
    position = 0
    
    while not [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input("Pick a Position ''(1 to 9)' : "))
        
    return position
        
        


def replay():
    
    return input("You wish to play again y or n : ").lower().startswith('y')




print('Welcome To the Game')

while True:
    
    the_board = [' '] * 10
    
    display_board(the_board)
        
    player1_marker, player2_marker = player_input()
    
    turn = first_turn()
    
    print(turn + " will go first")
    
    play_game = input("Are you ready to play? y or n : ")
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
                
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congrats, Player 1 won the game")
                    
                game_on = False
            else:
                    
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("Game is Tie")
                    break
                        
                else:
                    turn = 'player 2'
                        
        else:
                    
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
                
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congrats, Player 2 won the game")
                game_on = False
                           
            else:
                    
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("Game is Tie")
                    break
                        
                else:
                    turn = 'player 1'
                    
                        
    if not replay():
        break
