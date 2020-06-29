#import random

def print_game(game):
    """Print the current instance of the Board"""
    print(game[0],game[1],game[2])
    print(game[3],game[4],game[5])
    print(game[6],game[7],game[8])

def check_status(game):
    """Checks if a player won
        Returns an index for the print statement
        else returns -1"""
    #Horizontal Conditions
    for i in range(0,9,3):
        if (game[i] == game[i+1] and game[i] == game[i+2]):
            if (game[i] == '.'):
                return (-1)
            return i

    #Vertical Conditions
    for i in range(3):
        if (game[i] == game[i+3] and game[i] == game[i+6]):
            if (game[i] == '.'):
                return (-1)
            return i

    #Diagonal Condtions
    if (game[0] == game[4] and game[0] == game[8]):
        if (game[i] == '.'):
                return (-1)
        return i

    if (game[2] == game[4] and game[2] == game[6]):
        if (game[i] == '.'):
                return (-1)
        return i

    return (-1)

def play_a_new_game():

    """
    0 = Unoccupied
    1 = X
    2 = 0 
    """

    #Initial game status with
    game = ['.','.','.',
            '.','.','.',
            '.','.','.']

    print('New Game: \n')
    print_game(game)
    print('\n')

    i = 0
    flip = False

    valid_moves = [0,1,2,3,4,5,6,7,8]
    go = True

    while (i<9):

        if (not flip):
            print("X's Turn")

            while go:
                position = int(input('Pick a valid position to place X: '))
                if (position in valid_moves):
                    go = False
                    #ind = valid_moves.index(position)
                    del valid_moves[valid_moves.index(position)]
                print('Invalid Position!')
            go = True

            game[position - 1] = 'X'
            print_game(game)
            if (i >= 4):
                win = check_status(game)
                if (win != -1):
                    print('\n',game[win],' WON!')
                    print('GAME OVER!')
                    return
            flip = True
            i += 1
            if (i == 9):
                break

        if (flip):
            print("O's Turn")

            #position = int(input('Pick a valid position to place O: '))
            while go:
                position = int(input('Pick a valid position to place O: '))
                if (position in valid_moves):
                    go = False
                    #ind = valid_moves.index(position)
                    del valid_moves[valid_moves.index(position)]
                print('Invalid Position!')
            go = True

            game[position - 1] = 'O'
            print_game(game)
            if (i >= 4):
                win = check_status(game)
                if (win != -1):
                    print('\n',game[win],' WON!')
                    print('GAME OVER!')
                    return
            flip = False
            i += 1
            if (i == 9):
                break

        print('\n')

    print("DRAW!")

if __name__ == "__main__":
    play_a_new_game()