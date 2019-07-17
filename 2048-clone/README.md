# 2048-clone

This is an attempt to make a clone of 2048 for the terminal (play the original here https://play2048.co/). A of 2019-07-17, it is playable, but certain aspects of the gameplay are not exactly the same as the original:

* The direction is determined by Python's input() function. This means if you want to say move up, you have to enter 'k' (or 'w') and then hit enter. This slows down the gameplay compared to the online version.
* Because of how the grid is formatted, only a single character can be shown at a time. This means that the number displayed in the each box is n in 2 ** n (so, e.g., 256 is displayed as 8, since 256 == 2 ** 8) . 10 is displayed as 'X'. Currently I haven't made the game display anything about 2^10 (1024).
* There is currently no way to properly detect a game over (i.e., no more possible moves). That might come in the future.
* Unlike in the original version of the game, even if all tiles are moved as far as they can go in a single direction, you can still move in that direction, the effect being that another number will be placed in a blank location on the board.

Under the hood, there are some issues as well:

* Currently, for up--down movement, the game looks column-by-column to see if the cell contains a 0 (and row-by-row for left-right movement). If it does, it copies everything over by  one cell (and replaces the topmost cell with a 0). Right now, I have the game hard-coded to just do this three times. This has the virtue that it works, but it is not a very elegant solution; ideally what should happen is that the game should check to so see whether the cell is still 0 or not and only copy things if necessary.
