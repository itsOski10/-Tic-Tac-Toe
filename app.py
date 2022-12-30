class player:
    def __init__(self,gamer,choice):

        self.gamer = gamer
        self.choice = choice



def draw_board (board):
  # board is a list of strings representing the current state of the game
  # e.g. ['X', 'O', ' ', ' ', 'X', ' ', 'O', ' ', ' ']

  # print the top row of the board
  print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

  # print the separator row
  print('-----------')

  # print the middle row of the board
  print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])

  # print the separator row
  print('-----------')

  # print the bottom row of the board
  print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# test the function by drawing an empty board
draw_board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])


draw_board
