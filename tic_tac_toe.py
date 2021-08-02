def initialize(board):
  for i in range(9):
    board += '.' # Add the 9 '.' to the list
# This function modifies the board but does not return anything
def show(board):
  for i in range(len(board)):
    print('%s ' % board[i], end = ' ')
    if i > 0 and (i+1) % 3 == 0:
      print('\n',end='') # Print a new line every 3 squares
def main():
  board = []
  initialize(board)
  show(board)
main()
def checkwin(board):
  for i in range(3): 
    if (board[3*i] == board[3*i+1] and board[3*i+1] == board[3*i+2] and board[3*i] != '.'):
      return board[3*i]
  for i in range(3):
    if ( board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != '.'):
      return board[i]
    if (board[0] == board[4] and board[4] == board[8] and board[0] != '.'):
      return board[0]
    if (board[2] == board[4] and board[4] == board[6] and board[2] != '.'):
      return[2]
    for i in range(9):
      if board[i] == '.':
        return 'NF'
    return 'D'
def main():
  while True:
    board = []
    initialize(board)
    s = input('Press q to quit or X to begin : ')
    if s=="X":
      playgame(board)
    if s == 'q':
      break
  for i in range(min(len(s),9)):
    board[i] = s[i] # Set the board status from the string
  show(board)
  result = checkwin(board)
  if result == 'D':
    print('The game ends in a draw.')
  elif result == 'NF':
    print('The game has not finished.')
  else:
    print('Player {} wins the game.'.format(result))
    print('---------------------------')
main()
def playgame(board):
  while True:
  # Ask player X for a board spot
    while True:
      i = input('Player X: enter a board spot between 0 and 8: ')
      if i.isdigit() == False: # Input is not a number
        print('Invalid input. Try again.')
        continue
      i = int(i)
      if i < 0 or 8 < i: # Input is not between 0 and 8
        print('Invalid input. Try again.')
        continue
      if board[i] != '.':
        print('Board occupied. Try again.')
        continue
      else:
        board[i] = 'X' # Set this square to 'X'
        break # Stop the loop
      # Check board status
    show(board)
    if checkwin(board) != 'NF':
      return checkwin(board)
    # Ask player O for a board spot
    while True:
      i = input('Player O: enter a board spot between 0 and 8: ')
      if i.isdigit() == False: # Input is not a number
       print('Invalid input. Try again.')
       continue
      i = int(i)
      if i < 0 or 8 < i: # Input is not between 0 and 8
       print('Invalid input. Try again.')
       continue
      if board[i] != '.':
       print('Board occupied. Try again.')
       continue
      else:
       board[i] = '0' # Set this square to 'O'
       break # Stop the loop
    # Check board status
    show(board)
    if checkwin(board) != 'NF':
      return checkwin(board)
def cheese():
  while True:
    board = []
    initialize(board)
    show(board)
    s = input('Press q to quit or anything else to play TIC-TAC-TOE:')
    if s == 'q':
      break
    result = playgame(board)
    if result == 'D':
      print('The game ends in a draw.')
    else:
      print('Player {} wins the game.'.format(result))
main()
