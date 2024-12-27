def print_Board(Board):
    print()
    for i,row in enumerate(board):
        row_str=" "
        for j,value in enumerate(row):
            row_str+=value
            if j!=len(row)-1:
                row_str+=' | '
        print(row_str)

        if i!=len(board)-1:
            print('-----------')

def get_move(turn,board):
    while True:
        row=int(input("\nEnter Row :"))
        col=int(input("Enter Column :"))

        if row<1 or row>len(board):
            print('Invalid Row, Try Again!')
        elif col<1 or col>len(board[row-1]):
            print('Invalid Column, Try Again!')
        elif board[row-1][col-1]!=" ":
            print("Already Taken, Try Again!")
        else:
            break
    board[row-1][col-1]=turn

def check_win(board,turn):
    lines=[
        #rows
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        #columns
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        #Diagonals
        [(0,0),(1,1),(2,2)],
        [(2,2),(1,1),(0,0)],
        [(0,2),(1,1),(2,0)],
        [(2,0),(1,1),(0,2)],
    ]
    for line in lines:
        win=True
        for pos in line:
            row,col=pos
            if board[row][col]!=turn:
                win=False
                break
        if win:
            return True
    else:
        return False

board=[
    [" "," "," "],
    #-------------
    [" "," "," "],
    #-------------
    [" "," "," "],
]

turn='X'
turn_number=0
print_Board(board)
while turn_number<9:
    print(f"\n{turn} player's turn.\nSelect your move :")
    get_move(turn,board)
    print_Board(board)
    winner=check_win(board,turn)
    if winner:
        break
    if turn=='X':
        turn='O'
    else:
        turn='X'
    turn_number+=1

if turn_number==9:
    print("\nGame Tied, Play Again!")
else:
    print(f"\nThe Winner was {turn}")