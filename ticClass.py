#import random

class Tictactoe:
    def __init__(self, human):
        self.game = ['.','.','.','.','.','.','.','.','.']
        self.valid_moves = [0,1,2,3,4,5,6,7,8]
        self.human = human
        if (self.human == 'X'):
            self.cmpt = 'O'
        else:
            self.cmpt = 'X'

    def print_game(self):
        print(self.game[0],self.game[1],self.game[2])
        print(self.game[3],self.game[4],self.game[5])
        print(self.game[6],self.game[7],self.game[8])

    def move(self,position,player):
        self.game[position] = player
        del self.valid_moves[self.valid_moves.index(position)]

if __name__ == "__main__":
    hum = input('What you like to play as [X/O]: ').upper()
    t = Tictactoe(hum)
    t.print_game()
    move = int(input('Enter position: '))
    t.move(move,hum)
    t.print_game()