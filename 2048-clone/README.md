# 2048-clone

This is an attempt to make a clone of 2048 for the terminal (play the original here https://play2048.co/). A of 2019-07-18, it is playable, but certain aspects of the gameplay are not exactly the same as the original. Consider the following a to-do list:

* The direction is determined by Python's input() function. This means if you want to say move up, you have to enter 'k' (or 'w') and then hit enter. This slows down the gameplay compared to the online version.
* Because of how the grid is formatted, only a single character can be shown at a time. This means that the number displayed in the each box is n in 2 ** n (so, e.g., 256 is displayed as 8, since 256 == 2 ** 8). For n > 9, it uses roman letters A--F, as in hexadecimal. The game can count all the way up to 2 ** 15 (32768, represented as F).
* Unlike in the original version of the game, even if all tiles are moved as far as they can go in a single direction, you can still move in that direction, the effect being that another number will be placed in a blank cell on the board.
* There is currently no way to properly detect a game over (i.e., no more possible moves). That might come in the future. If the board if full and you try to move in a direction that does not create an open cell, you will get a game over.

Under the hood, there have been some issues as well, though those are starting to be cleared up!

* The routines for moving things into empty cells is no longer hard coded. These have been replaced with a while loop.
* The code for drawing the grid has been broken down a bit. It could still be cleaned up more, but that's not where I am with it.
* Fixed the behaviour adding new numbers to the grid. Now both 2 ** 1 and 2 ** 2 appear rather than just 2 ** 1.
