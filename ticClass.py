import random
from copy import deepcopy

class Game:
    def __init__(self, human):
        self.board = ['.','.','.','.','.','.','.','.','.']
        #self.valid_moves = [0,1,2,3,4,5,6,7,8]
        self.valid_moves = [1,2,3,4,5,6,7,8,9]
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
        print('\n')

    def move(self,position,player):
        self.board[position-1] = player
        del self.valid_moves[self.valid_moves.index(position)]
        #del self.valid_moves[position-1]

    def human_turn(self):
        while True:
            print('YOUR Turn\n')
            print('Pick one of the following valid positions:')
            print(self.valid_moves)
            movePos = input('\nPick a valid move: ')
            try:
                movePos = int(movePos)
            except:
                print('Please enter a number!\n')
                continue

            if (movePos in self.valid_moves):
                self.move(movePos,self.human)
                break
            else:
                print('Invalid Position')

    def cmpt_turn(self):
        print('COMPUTER\'S Turn')
        print('Calculating Move...')
        random_playout_board = deepcopy(self.board)
        current_moves = deepcopy(self.valid_moves)
        playout_score = []
        for i in current_moves:
            '''
            number in the inner loop range is the number of playouts
            '''
            total = 0
            for j in range(5000):
                """
                using 5000 random playouts to prevent forking
                """
                result = random_playouts(random_playout_board,i,self.human)
                #total keeps track of the points
                total += result

            playout_score.append(total)
        maxTotal = playout_score.index(max(playout_score))

        self.move(self.valid_moves[maxTotal],self.cmpt)

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
            return theBoard[2]

        if len(self.valid_moves) == 0:
            return 'draw'

        return False

def random_playouts(board,moves,human):
    '''
    Function to play random playouts
    '''
    if human == 'X':
        cmpt = 'O'
    else:
        cmpt = 'X'
    '''
    win = 2
    loss = -1
    draw = 1
    '''
    rand_board = deepcopy(board) #copy from an object
    rand_board[moves-1] = cmpt

    rand = Game(human) #create a new game for the random playouts
    rand.board = rand_board
    rand.valid_moves = curr_moves(rand.board)

    rand_human = False
    while True:
        if len(rand.valid_moves) == 0:
            return 1
        #random.seed()
        turn = random.choice(rand.valid_moves)#randomly choose a valid move
        if rand_human == True:
            rand.move(turn,cmpt)
        else:
            rand.move(turn,human)
        rand_human = not rand_human
        """
        The asigned weights are returned by the random playout function
        and are then added to the total score
        win = 2
        loss = -1
        draw = 0.5
        """

        if rand.check_win() == cmpt:
            return 1
        elif rand.check_win() == human:
            return 0
        elif rand.check_win() == 'draw':
            return 0.5
        else:
            continue
        #reloop if no result

"""Created to return valid_moves to random_playouts function"""
def curr_moves(board):
    curr = []
    j = 0
    for i in board:
        if i == '.':
            curr.append(j+1)
        j+=1

    return curr


def play_again():
    while True:
        again = input('\nWould you like to play again? [Y/N]: ').upper()
        if (again == 'Y' or again == 'N'):
            if again == 'Y':
                return True
            else:
                return False
        else:
            print('Invalid Input!')

def play_a_new_game():

    again = True

    while again:

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
        Tic = Game(start)

        print('Starting Board:')
        Tic.print_board()

        #Humans goes first
        if start == 'X':
            while True:
                Tic.human_turn()
                Tic.print_board()

                if (Tic.check_win() == Tic.human):
                    print('YOU WIN!')
                    break

                if (Tic.check_win() == Tic.cmpt):
                    print('COMPUTER WINS!')
                    break

                if (Tic.check_win() == 'draw'):
                    print('DRAW!')
                    break

                Tic.cmpt_turn()
                Tic.print_board()

                if (Tic.check_win() == Tic.human):
                    print('YOU WIN!')
                    break

                if (Tic.check_win() == Tic.cmpt):
                    print('COMPUTER WINS!')
                    break

                if (Tic.check_win() == 'draw'):
                    print('DRAW!')
                    break

        #computer goes first
        else:
            while True:
                Tic.cmpt_turn()
                Tic.print_board()

                if (Tic.check_win() == Tic.human):
                    print('======\nYOU WIN!\n======')
                    break

                if (Tic.check_win() == Tic.cmpt):
                    print('======\nCOMPUTER WINS!\n======')
                    break

                if (Tic.check_win() == 'draw'):
                    print('======\nDRAW!\n======')
                    break

                Tic.human_turn()
                Tic.print_board()

                if (Tic.check_win() == Tic.human):
                    print('======\nYOU WIN!\n======')
                    break

                if (Tic.check_win() == Tic.cmpt):
                    print('======\nCOMPUTER WINS!\n======')
                    break

                if (Tic.check_win() == 'draw'):
                    print('======\nDRAW!\n======')
                    break

        again = play_again()


if __name__ == "__main__":
    play_a_new_game()