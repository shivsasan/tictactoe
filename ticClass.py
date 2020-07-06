#import random

class Game:
    def __init__(self, human):
        self.board = ['.','.','.','.','.','.','.','.','.']
        self.valid_moves = [0,1,2,3,4,5,6,7,8]
        self.human = human
        if (self.human == 'X'):
            self.cmpt = 'O'
        else:
            self.cmpt = 'X'

    def print_board(self):
        print('\n')
        print(self.board[0],self.board[1],self.board[2])
        print(self.board[3],self.board[4],self.board[5])
        print(self.board[6],self.board[7],self.board[8])

    def move(self,position,player):
        self.board[position] = player
        del self.valid_moves[self.valid_moves.index(position)]

    def check_win(self):

        """
        This functions checks whether a game is over or not 
        and returns the winning player
        """

        #horizontal conditions
        theBoard = self.board

        for i in range(0,9,3):
            if(theBoard[i] == theBoard[i+1] and theBoard [i] == theBoard[i+2]):
                if(theBoard[i] == '.'):
                    return False  #return false if no one wins
                return theBoard[i] #return the character at the winning tile
        
        #vertical conditions
        for i in range(3):
            if (theBoard[i] == theBoard[i+3] and theBoard[i] == theBoard [i+6]):
                if(theBoard[i] == '.'):
                    return False
                return theBoard[i]
        
        #diagonal conditions
        if (theBoard[0] == theBoard[4] and theBoard[0] == theBoard[8]):
            if(theBoard[0] == '.'):
                return False
            return theBoard[0]

        if (theBoard[2] == theBoard[4] and theBoard[2] == theBoard[6]):
            if(theBoard[2] == '.'):
                return False
            return theBoard[0]

        return False

def play_again():
    while True:
        again = input('Would you like to play again? [Y/N]: ').upper()
        if (again == 'Y' or again == 'N'):
            if again == 'Y':
                return True
            else:
                return False
        else:
            print('Invalid Input!')

def play_a_new_game():

    print('\nWelcome to Tic-Tac-Toe')
    print('Attacker starts first\n')
    print('X = attacker \nO = defender\n')

    while True:
        start = input('Would you like to attack or defend? [X/O]: ').upper()
        if (start == 'X' or start == 'O'):
            break
        else:
            print('Invalid Input!')

    #create a new game
    print('Lets Start!')
    T = Game(start)
    T.print_board()
    print('Valid Moves: ',T.valid_moves)
    move = int(input('pick a valid move: '))
    T.move(move,T.human)
    T.print_board()
    print(T.valid_moves)


if __name__ == "__main__":
        play_a_new_game()