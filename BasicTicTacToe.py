board=["_","_","_","_","_","_","_","_","_"]
GameRunning=True
winner='N'
Current='X'

def Tie():
  
  global GameRunning
  if "_" not in board:
    GameRunning = False
    return True
  else:
    return False

def Rows():
  
  global GameRunning

  row_1 = board[0] == board[1] == board[2] != "_"
  row_2 = board[3] == board[4] == board[5] != "_"
  row_3 = board[6] == board[7] == board[8] != "_"

  if row_1 or row_2 or row_3:
    GameRunning = False

  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  else:
    return 'N'


def Columns():
  
  global GameRunning
  column_1 = board[0] == board[3] == board[6] != "_"
  column_2 = board[1] == board[4] == board[7] != "_"
  column_3 = board[2] == board[5] == board[8] != "_"
  
  if column_1 or column_2 or column_3:
    GameRunning = False
  
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  else:
    return 'N'


def Diagonals():

  global GameRunning 
  diagonal_1 = board[0] == board[4] == board[8] != "_"
  diagonal_2 = board[2] == board[4] == board[6] != "_"
  if diagonal_1 or diagonal_2:
    GameRunning = False
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  else:
    return 'N'


def IsWon():
    if( Rows()!='N' ):
        return Rows()
    if( Columns()!='N' ):
        return Columns()
    if( Diagonals()!='N' ):
        return Diagonals()
    else:
        return 'N'


def IsOver():
    global GameRunning
    global winner
    if(IsWon()=='N'):
        if(Tie()==True):
            GameRunning=False
    else:
        winner=IsWon()


def DisplayBoard():
    print()
    print("|",board[0],"|",board[1],"|",board[2],"    1|2|3")
    print("|",board[3],"|",board[4],"|",board[5],"    4|5|6")
    print("|",board[6],"|",board[7],"|",board[8],"    7|8|9")
    print()


def ChangeTurn():

  global Current
  if Current == 'X':
    Current = 'O'
  elif Current == 'O':
    Current = 'X'

def Play():
    
    global Current
    global winner
    while(GameRunning==True):
        DisplayBoard()
        TakeTurn(Current)
        IsOver()
        ChangeTurn()

    if(winner=='X' or winner=='O'): print(winner,"won the game!")
    elif(winner=='N'): print("It's a tie")


def TakeTurn(player):
    print(player,"'s turn")
    position=int(input("Choose a position from 1 to 9 "))
    position-=1
    if position in [0,1,2,3,4,5,6,7,8]:
        if(board[position]=='_'):
          board[position]=player
    else:
        print("Invalid Input")
    DisplayBoard()

Play()










