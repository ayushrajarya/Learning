#6
def print_board(board_in):
    for i in board_in:
        print(" ".join(i))
"""
Join method for joining strings
"""
board= []
for i in range(5):
    board.append(["O"]*5)
print_board(board)

#10
from random import randint
def print_board(board_in):
    for i in board_in:
        print(" ".join(i))
"""
Join method for joining strings
"""
def random_row(board_in):
    return randint(0,len(board_in)-1)
def random_col(board_in):
    return randint(0,len(board_in)-1)
board= []
for i in range(5):
    board.append(["O"]*5)
print_board(board)
ship_row=random_row(board)
ship_col=random_col(board)
print(ship_row)
print(ship_col)
guess_row = int(input("Guess Row: "))
guess_col= int(input("Guess Col: "))

#14
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row==ship_row and guess_col== ship_col:
  print("Congratulations! You sank my battleship!")
elif guess_col not in range(5) or guess_row not in range(5):
  print("Oops, that's not even in the ocean.")
elif board[guess_row][guess_col]== "X":
  print("You guessed that one already.")
else:
  print("You missed my battleship!")
  board[guess_row][guess_col]="X"
  print_board(board)


guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

if guess_row==ship_row and guess_col== ship_col:
  print("Congratulations! You sank my battleship!")
elif guess_col not in range(5) or guess_row not in range(5):
  print("Oops, that's not even in the ocean.")
elif board[guess_row][guess_col]== "X":
  print("You guessed that one already.")
else:
  print("You missed my battleship!")
  board[guess_row][guess_col]="X"
  print_board(board)

#19
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print("Turn", turn+1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  # Write your code below!
  if guess_row==ship_row and guess_col== ship_col:
    print("Congratulations! You sank my battleship!")
    print("Game Over")
    break
  elif guess_col not in range(5) or guess_row not in range(5):
    print("Oops, that's not even in the ocean.")
    if turn==3:
      print("Game Over")
  elif board[guess_row][guess_col]== "X":
    print("You guessed that one already.")
    if turn==3:
      print("Game Over")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col]="X"
    print_board(board)
    if turn==3:
      print("Game Over")