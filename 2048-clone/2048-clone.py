#!/bin/python3

""" 
A 2048 clone for the terminal!
(C) 2019 Nicholas LaCara

A proof of concept, anyway...
"""
from random import randint      #For inserting random numbers into the grid.

## A few of these are for testing purposes.
#start_grid = [[4, 0, 3, 2], [4, 1, 0, 0], [4, 0, 2, 0], [4, 0, 0, 2]]
#start_grid = [[1, 0, 4, 8], [1, 0, 0, 4], [0, 0, 3, 4], [0, 0, 0, 4]]
#start_grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
#start_grid = [[1, 1, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

start_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

grid = start_grid
""" Here we have some commands for drawing the grid """

def draw_grid():
    """ Draws a 2048 grid """
    print(" ")
    print(" ", "\u2554\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2557")
    print(f"  \u2551 {grid[0][0]} \u2502 {grid[0][1]} \u2502 {grid[0][2]} \u2502 {grid[0][3]} \u2551".replace("10", "X").replace("0", " "))
    print(" ", "\u255f\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2562")
    print(f"  \u2551 {grid[1][0]} \u2502 {grid[1][1]} \u2502 {grid[1][2]} \u2502 {grid[1][3]} \u2551".replace("10", "X").replace("0", " "))
    print(" ", "\u255f\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2562")
    print(f"  \u2551 {grid[2][0]} \u2502 {grid[2][1]} \u2502 {grid[2][2]} \u2502 {grid[2][3]} \u2551".replace("10", "X").replace("0", " "))
    print(" ", "\u255f\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2562")
    print(f"  \u2551 {grid[3][0]} \u2502 {grid[3][1]} \u2502 {grid[3][2]} \u2502 {grid[3][3]} \u2551".replace("10", "X").replace("0", " "))
    print(" ", "\u255a\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u255d")
    print("Score: ", get_score())
    print(" ")
    
def get_score():
    """ Determine the game score from the numbers in the grid. """
    score = []
    
    for row in grid:
        for cell in row:
            if cell > 0:
                score.append(2 ** cell)
    return sum(score)

""" We need a way to add numbers to the grid """ 
def add_number():
    """ Adds a random number to the grid. """
    zeros = []
    
    # First, figure out which cells are zeros in the grid.
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 0:
                zeros.append([row, col])
    if len(zeros) == 0:
        game_over()
    else:
        # Now, select one of these to be the place insert the new number.
        index = randint(0, len(zeros) - 1)
        cell = zeros[index]
        grid[cell[0]][cell[1]] = 1
        

""" The following are commands for handing movement. """
    
def move_down():
    """ Move everything down and sum. """
    
    def cell_down(row, col):
        """ Moves everything to the lowest row possible. """
        if grid[row][col] == 0:
            for k in range(0, row):
                grid[row - k][col] = grid[row - k - 1][col]
                grid[row - k - 1][col] = 0
            grid[0][col] = 0
            
        # Calling this recursively has not been working, so brute forcing for now.
        if grid[row][col] == 0:
            for k in range(0, row):
                grid[row - k][col] = grid[row - k - 1][col]
                grid[row - k - 1][col] = 0
            grid[0][col] = 0

        if grid[row][col] == 0:
            for k in range(0, row):
                grid[row - k][col] = grid[row - k - 1][col]
                grid[row - k - 1][col] = 0
            grid[0][col] = 0

                
    def cell_add(row, col):
        """ Sum the contents of two cells with the same values """
        if grid[row][col] == grid[row - 1][col] and grid[row][col] > 0:
            
            grid[row][col] += 1
            grid[row - 1][col] = 0
    

                
    #print("===== Merging down =====")
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = 3 - r
            cell_down(row, col)

    
    #print("===== Adding =====")
    for c in range (0,4):
        col = c
        
        for r in range (0, 3):
            row = 3 - r
            cell_add(row, col)
   

    #print("===== Merging down again =====")
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
            for k in range(0, 3 - row):
                grid[row + k][col] = grid[row + k + 1][col]
                grid[row + k + 1][col] = 0
            grid[3][col] = 0
            
        # Calling this recursively has not been working, so brute forcing for now.
        if grid[row][col] == 0:
            for k in range(0, 3 - row):
                grid[row + k][col] = grid[row + k + 1][col]
                grid[row + k + 1][col] = 0
            grid[3][col] = 0
            
        if grid[row][col] == 0:
            for k in range(0, 3 - row):
                grid[row + k][col] = grid[row + k + 1][col]
                grid[row + k + 1][col] = 0
            grid[3][col] = 0
            
            

                
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
        if grid[row][col] == 0:
            for k in range(0, col):
                grid[row][col - k] = grid[row][col - k - 1]
                grid[row][col - k - 1] = 0
                
            grid[row][0] = 0
            
        if grid[row][col] == 0:
            for k in range(0, col):
                grid[row][col - k] = grid[row][col - k - 1]
                grid[row][col - k - 1] = 0
                
            grid[row][0] = 0

        if grid[row][col] == 0:
            for k in range(0, col):
                grid[row][col - k] = grid[row][col - k - 1]
                grid[row][col - k - 1] = 0
                
            grid[row][0] = 0

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
        """ Moves everything to the highest row possible. """
        if grid[row][col] == 0:
            for k in range(0, 3 - col):
                grid[row][col + k] = grid[row][col + k + 1]
                grid[row][col + k + 1] = 0
                
            grid[row][3] = 0
            
        if grid[row][col] == 0:
            for k in range(0, 3 - col):
                grid[row][col + k] = grid[row][col + k + 1]
                grid[row][col + k + 1] = 0
                
            grid[row][3] = 0
            
        if grid[row][col] == 0:
            for k in range(0, 3 - col):
                grid[row][col + k] = grid[row][col + k + 1]
                grid[row][col + k + 1] = 0
                
            grid[row][3] = 0
            

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
        
""" The following method should play the game. """

def play_game():
    
    while True:
        add_number()
        draw_grid()
        get_direction()
        

            
play_game()
