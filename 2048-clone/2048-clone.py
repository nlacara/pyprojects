#!/bin/python3

""" 
A 2048 clone for the terminal!
(C) 2019 Nicholas LaCara

A proof of concept, anyway...
"""
from random import randint      #For inserting random numbers into the grid.

# These are for testing purposes.
test_grid_0 = [[4, 0, 3, 2], [4, 1, 0, 0], [4, 0, 2, 0], [4, 0, 0, 2]]
test_grid_1 = [[1, 0, 4, 8], [1, 0, 0, 4], [0, 0, 3, 4], [0, 0, 0, 4]]
test_grid_2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
test_grid_3 = [[1, 1, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
test_grid_4 = [[0, 1, 2, 3], [7, 6, 5, 4], [8, 9, 10, 11], [15, 14, 13, 12]]

# This is a blank grid for starting a new game.
start_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

grid = start_grid

""" Here we have some commands for drawing the grid """

def row_print(grid, row):
    print(f"  \u2551 {grid[row][0]} \u2502 {grid[row][1]} \u2502 {grid[row][2]} \u2502 {grid[row][3]} \u2551".replace("10", "A").replace("11", "B").replace("12", "C").replace("13", "D").replace("14", "E").replace("15", "F").replace("0", " "))

def hline():
    """ Horizontal line in the grid."""
    print(" ", "\u255f\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2562")
    
def tline():
    """ Top line of the grid """
    print(" ", "\u2554\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2557")

    
def bline():
    """ Bottom line of the grid."""
    print(" ", "\u255a\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u255d")

def draw_grid():
    """ Draws a 2048 grid. ASCII-style box art here in the style of old DOS games. """
    print(" ")
    tline()
    row_print(grid, 0)
    hline()
    row_print(grid, 1)
    hline()
    row_print(grid, 2)
    hline()
    row_print(grid, 3)
    bline()
    # Add the score at the bottom.
    print("Score: ", get_score())
    print(" ")
    
def get_score():
    """ Determine the game score from the numbers in the grid. I'm not really sure how 2048 actuall scores its game; this just tallies the total value of numbers in the grid."""
    score = []
    
    for row in grid:
        for cell in row:
            if cell > 0:
                score.append(2 ** cell)
    return sum(score)

def add_number():
    """ Adds a random number to the grid. This gets called at the beginning of every turn."""
    zeros = []
    
    # First, figure out which cells are zeros in the grid.
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 0:
                zeros.append([row, col])
    if len(zeros) == 0:
        game_over()
    else:
        # Now, select one of these to be the place insert the new number (either 1 or 2).
        index = randint(0, len(zeros) - 1)
        new_num = randint(1,2)
        cell = zeros[index]
        grid[cell[0]][cell[1]] = new_num
        

# The following are commands for handing movement.
# There's probably a way to reduce these to a single function,
# but I'll leave that to the future.
    
def move_down():
    """ Move everything down and sum. """
    
    def cell_down(row, col):
        """ Moves everything to the lowest row possible. """
        if grid[row][col] == 0:
            j_sum = 0
            for j in range(0, row):
                j_sum += grid[j][col]

            # print(j_sum)
            # wait = input("Waiting")
            if j_sum > 0:
                # print(f"{col}, {row} is a 0!")
                while grid[row][col] == 0:
                    for k in range(0, row):
                        # print(f"Moving {col} , {row - k - 1} to {[col]}, {[row - k]}")
                        grid[row - k][col] = grid[row - k - 1][col]
                        grid[row - k - 1][col] = 0
                    grid[0][col] = 0
                else:
                    pass
            
    def cell_add(row, col):
        """ Sum the contents of two cells with the same values """
        if grid[row][col] == grid[row - 1][col] and grid[row][col] > 0:
            
            grid[row][col] += 1
            grid[row - 1][col] = 0
    

                
    # Move everything down.
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = 3 - r
            cell_down(row, col)

    
    # Add cells together.
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = 3 - r
            cell_add(row, col)
   
    # Move everything down again.
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = 3 - r
            cell_down(row, col)
            


def move_up():
    """ Move everything up and sum. """
    
    def cell_up(row, col):
        """ Moves everything to the highest row possible. """
        if grid[row][col] == 0:
            j_sum = 0
            for j in range(row + 1, 4):
                j_sum += grid[j][col]

            # print(j_sum)
            # wait = input("Waiting")
            if j_sum > 0:
                # print(f"{col}, {row} is a 0!")
                while grid[row][col] == 0:
                    for k in range(0, 3 - row):
                        grid[row + k][col] = grid[row + k + 1][col]
                        grid[row + k + 1][col] = 0
                    grid[3][col] = 0
                else:
                    pass
            
                
    def cell_add(row, col):
        """ Sum the contents of two cells with the same values """
        if grid[row][col] == grid[row + 1][col] and grid[row][col] > 0:
            
            grid[row][col] += 1
            grid[row + 1][col] = 0
    

                
    #print("===== Merging up =====")
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = r
            cell_up(row, col)
    
    #print("===== Adding =====")
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = r
            cell_add(row, col)
   
    #print("===== Merging down up =====")
    for c in range(0,4):
        col = c
        
        for r in range(0, 3):
            row = 3 - r
            cell_up(row, col)
            
    
def move_right():
    
    def cell_right(row, col):
        """ Moves everything to the rightmost col possible. """
        if grid[row][col] == 0:
            j_sum = 0
            j_list = []
            for j in range(0, col):
                j_sum += grid[row][j]
                j_list.append(grid[row][j])
                
            if j_sum > 0:
                while grid[row][col] == 0:
                    for k in range(0, col):
                        grid[row][col - k] = grid[row][col - k - 1]
                        grid[row][col - k - 1] = 0
                        
                    grid[row][0] = 0            
                else:
                    pass
            
                
    def cell_add(row, col):
        """ Sum the contents of two cells with the same values """
        if grid[row][col] == grid[row][col - 1] and grid[row][col] > 0:
            grid[row][col] += 1
            grid[row][col - 1] = 0
            
   
    #print("===== Merging right =====")
    for r in range (0, 4):
        row = r
        
        for c in range (0,4):
            col = 3 - c
            cell_right(row, col)
        
    #print("===== Adding =====")
    for c in range (0,4):
        col = 3 - c
        
        for r in range (0, 4):
            row = r
            cell_add(row, col)
   
    #print("===== Merging right again =====")
    for r in range (0, 4):
        row = r
        
        for c in range (0,4):
            col = 3 - c
            cell_right(row, col)
        
            
def move_left():
    
    def cell_left(row, col):
        """ Moves everything to the rightmost col possible. """
        if grid[row][col] == 0:
            j_sum = 0
            for j in range(col + 1, 4):
                j_sum += grid[row][j]
                #print(j_sum)
            #print(j_sum)
            #wait = input("Waiting")
            if j_sum > 0:
                while grid[row][col] == 0:
                    for k in range(0, 3 - col):
                        grid[row][col + k] = grid[row][col + k + 1]
                        grid[row][col + k + 1] = 0
                        
                    grid[row][3] = 0            
                else:
                    pass
            
                
    def cell_add(row, col):
        """ Sum the contents of two cells with the same values """
        if grid[row][col] == grid[row][col + 1] and grid[row][col] > 0:
            grid[row][col] += 1
            grid[row][col + 1] = 0
   
    #print("===== Merging right =====")
    for r in range (0, 4):
        row = r
        
        for c in range (0,4):
            col = c
            #print(f"Now at column {col}.")
            cell_left(row, col)
        
    #print("===== Adding =====")
    for c in range (0,3):
        col = c
        #print(f"Now at column {col}.")
        
        for r in range (0, 4):
            row = r
            cell_add(row, col)
   
    #print("===== Merging right again =====")
    for r in range (0, 4):
        row = r
        
        for c in range (0,4):
            col = c
            #print(f"Now at column {col}.")
            cell_left(row, col)
        

""" Game controls   """

def get_direction():
    
    direction = input("[H/A - Left | J/S - Down | K/W - Up | D/L - Right | Q - Quit] > ").upper()
    
    if direction == "J" or direction == "S" :
        move_down()
    elif direction == "K" or direction == "W" :
        move_up()
    elif direction == "L" or direction == "D" :
        move_right()
    elif direction == "H" or direction == "A" :
        move_left()
    elif direction == "Q":
        exit()
    else:
        get_direction()
        
def game_over():
    print("Game Over!")
    exit()
        
""" The following method should play the game. """

def play_game():
    
    while True:
        add_number()
        draw_grid()
        get_direction()
        

            
play_game()
