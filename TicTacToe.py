#tic tac toe
import random
import time

positions = list(' ' * 9)
player = 'O'
computer = 'O'
player_moved = False

def print_board():
    global positions
    print("     |     |     ")
    print("  " + positions[0] + "  |  " + positions[1] + "  |  " + positions[2])
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + positions[3] + "  |  " + positions[4] + "  |  " + positions[5])
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + positions[6] + "  |  " + positions[7] + "  |  " + positions[8])
    print("     |     |     ")

def get_move():
    global player_moved
    global positions
    choice = False
    global player
    while choice == False:
        move = int(input("What square would you like to play? "))
        if positions[move - 1] == ' ':
            positions[move -1] = player
            choice = True
            player_moved = True
        else:
            print("Not a valid square")
    

def is_winning_move(positions, player):
    if positions[0] and positions[1] and positions[2] == player: #top
        return True
    elif positions[0] and positions[3] and positions[6] == player: #left down
        return True
    elif positions[3] and positions[4] and positions[5] == player: #middle
        return True
    elif positions[6] and positions[7] and positions[8] == player: #bottom
        return True
    elif positions[2] and positions[5] and positions[8] == player: #right down
        return True
    elif positions[1] and positions[4] and positions[7] == player: #middle down
        return True
    elif positions[6] and positions[4] and positions[2] == player: #across right
        return True    
    elif positions[0] and positions[4] and positions[8] == player: #across left
        return True
    else:
        return False

def make_random_move():
    global positions
    global computer
    count = 0
    move = 0
    while count < 10:
        move = random.randint(-1, 8)
        if positions[move] == ' ':
            positions[move] = computer
            break
def get_board_copy(board):
    dupe = []
    for i in board:
        board.append(i)

    return dupe
        
    
def computer_move():
    print("The computer is thinking...")
    time.sleep(1)
    global positions
    global computer
    global player

    for move in range(0, 8):
        copy = get_board_copy(positions)
        if copy[move] == ' ':
            copy[move] = computer
            if is_winning_move(copy, computer):
                return move
    return none
        
 


print_board()
get_move()
print_board()
get_move()
print_board()
positions[computer_move()] = 'X'
print_board()

     

