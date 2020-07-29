import math
import timeit

start = timeit.default_timer()

board = [
    # [0,6,0,3,0,0,8,0,4],
    # [5,3,7,0,9,0,0,0,0],
    # [0,4,0,0,0,6,3,0,7],
    # [0,9,0,0,5,1,2,3,8],
    # [0,0,0,0,0,0,0,0,0],
    # [7,1,3,6,2,0,0,4,0],
    # [3,0,6,4,0,0,0,1,0],
    # [0,0,0,0,6,0,5,2,3],
    # [1,0,2,0,0,9,0,8,0]


    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

# Print out a board for viewing based on a string input of Sudoko coordinates
def display_board(board):
    for i in range(len(board)):
        if (i)%3 == 0 or i == 0:   
            print('-------------------------')
        
        for j in range(len(board[i])):
            if (j)%3 == 0 or j == 0 and j != 8:   
                print('|' + ' ', end = '')
                print(str(board[i][j]) + ' ', end = '')
            elif j == 8:
                print(str(board[i][j]) + ' ', end = '')
                print('|')
            else:
                print(str(board[i][j]) + ' ', end = '')

        if i == 8:
            print('-------------------------')

# Iterate through board and locate blank spaces (zeros)
def find_zeros(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i,j
    return None
            

# Determine if a certain number at a given location is legal
def legal_move(board, number, coord):
    x,y = coord  # seperate tuple
    tot_sum = 0

    # Determine if there is any errors within the column
    z = 0
    for j in range(len(board)):
        if board[x][j] == number:
            z += 1
    if z >= 1:
        tot_sum += 1        

    # Determine if there is any errors within the row  
    z = 0
    for i in range(len(board)):
        if board[i][y] == number:
            z += 1
    if z >= 1:
        tot_sum += 1    

    # Determine if there is any errors within the 3 x 3 box
    x1 = math.floor(x/3)
    y1 = math.floor(y/3)
    z = 0
    for i in range(3):
        for j in range(3):
            if board[(x1*3)+i][(y1*3)+j] == number:
                z += 1
    if z >= 1:
        tot_sum += 1 
    
    if tot_sum >= 1:
        return False
    else:
        return True

# Backtrack through possible solutions to arrive at final answer
def solve(board):

    # Find the first empty square in the puzzle
    if find_zeros(board) == None:
        return True
    x,y = find_zeros(board)

    # Try every number until you find a number that fits
    for i in range(1,10):
        if legal_move(board,i,(x,y)) == True:
            board[x][y] = i   # Assign that number to the empty box

            # Use recursion to rerun the same function
            if solve(board) == True:
                return True

            # If there is no solution, reset the previous answer to zero and reset (backtracking)
            board[x][y] = 0

    return False

# Solve board and display solution
solve(board)
display_board(board)

stop = timeit.default_timer()

print('Time: ', stop - start)