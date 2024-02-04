# Tusmo Solver

Tusmo is a famous word puzzle, that works on the same principles as Wordle. Using basic notions of statistics and information theories, this solver gives the user propositions that may alllow him to solve these puzzles. It can be noted that the notions used are not the exact same as the ones used by 3Blue1Brown and ScienceEtonante in their respective videos about the subject.

## Overview

The files are written here in python, and the words database is stored in a CSV file. There are 2 files that can be executed:

- main.py, to use the solver
- jouer.py, to play to a simple copy of the game

Whether in one file or the other, the results are given with the same code: 2 if the letter is in the right place, 1 if there is this letter but not in this place and 0 if this letter is not in this place. Both the files using a textual interface within the console.

## Principles

The algorithm works in two stages, which are repeated throughout the different trials. First, it selects only the possible words according to the current knowledge, and then it select the word among all the others that give the most of information about the possible words selected earlier.
The difference between this algorithm and the ones presented in the videos introduced earlier is in the functiun that determines the quantity of information given by a guess. While in the videos the function relie on solid math concepts, here, it is a simple heuristic function.
This function give for each letter of the guess a number depending on whether it is in the right place, in the word but not in the right place, or not in the word (2,1 and 0 in the code), and then return the sum of these numbers, divided by the length of the word. The score for each word is in fact the average of the score for each of its letters.
