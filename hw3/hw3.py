##############
# Homework 3 #
##############


###################
# Read This First #
###################


# All functions that you need to modify are marked with 'EXERCISE' in their header comments.
# Do not modify astar.py
# This file also contains many helper functions. You may call any of them in your functions.


# Due to the memory limitation, the A* algorithm may crash on some hard sokoban problems if too many
# nodes are generated. Improving the quality of the heuristic will mitigate
# this problem, as it will allow A* to solve hard problems with fewer node expansions.


# Remember that most functions are not graded on efficiency (only correctness).
# Efficiency can only influence your heuristic performance in the competition (which will affect your score).


# Load the astar.py and do not modify it.
import astar
# Load the numpy package and the state is represented as a numpy array during this homework.
import numpy as np


# a_star perform the A* algorithm with the start_state (numpy array), goal_test (function), successors (function) and
# heuristic (function). a_star prints the solution from start_state to goal_state (path), calculates the number of
# generated nodes (node_generated) and expanded nodes (node_expanded), and the solution depth (len(path)-1). a_star
# also provides the following functions for printing states and moves: prettyMoves(path): Translate the solution to a
# list of moves printlists(path): Visualize the solution and Print a list of states
def a_star(start_state, goal_test, successors, heuristic):
    goal_node, node_generated, node_expanded = astar.a_star_search(start_state, goal_test, successors, heuristic)
    if goal_node:
        node = goal_node
        path = [node.state1]
        while node.parent:
            node = node.parent
            path.append(node.state1)
        path.reverse()

        # print('My path:{}'.format(path))
        # print(prettyMoves(path))
        # printlists(path)
        print('Nodes Generated by A*: {}'.format(node_generated))
        print('Nodes Expanded by A*: {}'.format(node_expanded))
        print('Solution Depth: {}'.format(len(path) - 1))
    else:
        print('no solution found')


# A shortcut function
# Transform the input state to numpy array. For other functions, the state s is presented as a numpy array.
# Goal-test and next-states stay the same throughout the assignment
# You can just call sokoban(init-state, heuristic function) to test the result
def sokoban(s, h):
    return a_star(np.array(s), goal_test, next_states, h)


# Define some global variables
blank = 0
wall = 1
box = 2
keeper = 3
star = 4
boxstar = 5
keeperstar = 6


# Some helper functions for checking the content of a square
def isBlank(v):
    return (v == blank)


def isWall(v):
    return (v == wall)


def isBox(v):
    return (v == box)


def isKeeper(v):
    return (v == keeper)


def isStar(v):
    return (v == star)


def isBoxstar(v):
    return (v == boxstar)


def isKeeperstar(v):
    return (v == keeperstar)


# Help function for get KeeperPosition
# Given state s (numpy array), return the position of the keeper by row, col
# The top row is the zeroth row
# The first (right) column is the zeroth column
def getKeeperPosition(s):
    row = s.shape[0]
    col = s.shape[1]
    for i in range(row):
        for j in range(col):
            if (isKeeper(s[i, j]) or isKeeperstar(s[i, j])):
                return i, j


# For input list s_list, remove all None element
# For example, if s_list = [1, 2, None, 3], returns [1, 2, 3]
def cleanUpList(s_list):
    clean = []
    for state in s_list:
        if state is not None:
            clean.append(state)
    return clean


# EXERCISE: Modify this function to return Ture
# if and only if s (numpy array) is a goal state of a Sokoban game.
# (no box is on a non-goal square)
# Remember, the number of goal can be larger than the number of box.
# Currently, it always returns False. If A* is called with
# this function as the goal testing function, A* will never
# terminate until the whole search space is exhausted.
def goal_test(s):
    raise NotImplementedError()


# EXERCISE: Modify this function to return the list of
# successor states of s (numpy array).
#
# This is the top-level next-states (successor) function.
# Some skeleton code is provided below.
# You may delete them totally, depending on your approach.
# 
# If you want to use it, you will need to set 'result' to be 
# the set of states after moving the keeper in each of the 4 directions.
#
# You can define the function try-move and decide how to represent UP,DOWN,LEFT,RIGHT.
# Any None result in the list can be removed by cleanUpList.
#
# When generated the successors states, you may need to copy the current state s (numpy array).
# A shallow copy (e.g, direcly set s1 = s) constructs a new compound object and then inserts references 
# into it to the objects found in the original. In this case, any change in the numpy array s1 will also affect
# the original array s. Thus, you may need a deep copy (e.g, s1 = np.copy(s)) to construct an indepedent array.
def next_states(s):
    row, col = getKeeperPosition(s)
    s_list = []
    s1 = np.copy(s)

    # NOT IMPLEMENTED YET! YOU NEED TO FINISH THIS FUNCTION.

    return cleanUpList(s_list)


# EXERCISE: Modify this function to compute the trivial
# admissible heuristic.
def h0(s):
    raise NotImplementedError()


# EXERCISE: Modify this function to compute the
# number of misplaced boxes in state s (numpy array).
def h1(s):
    raise NotImplementedError()


# EXERCISE: 
# This function will be tested in various hard examples.
# Objective: make A* solve problems as fast as possible.

def h2(s):
    raise NotImplementedError()


# Some predefined problems with initial state s (array). Sokoban function will automatically transform it to numpy
# array. For other function, the state s is presented as a numpy array. You can just call sokoban(init-state,
# heuristic function) to test the result Each problem can be visualized by calling prettyMoves(path) and printlists(
# path) in a_star function
#
# Problems are roughly ordered by their difficulties.
# For most problems, we also provide 2 additional number per problem:
#    1) # of nodes expanded by A* using our next-states and h0 heuristic.
#    2) the depth of the optimal solution.
# These numbers are located at the comments of the problems. For example, the first problem below 
# was solved by 80 nodes expansion of A* and its optimal solution depth is 7.
# 
# Your implementation may not result in the same number of nodes expanded, but it should probably
# give something in the same ballpark. As for the solution depth, any admissible heuristic must 
# make A* return an optimal solution. So, the depths of the optimal solutions provided could be used
# for checking whether your heuristic is admissible.
#
# Warning: some problems toward the end are quite hard and could be impossible to solve without a good heuristic!


# [80,7]
s1 = [[1, 1, 1, 1, 1, 1],
      [1, 0, 3, 0, 0, 1],
      [1, 0, 2, 0, 0, 1],
      [1, 1, 0, 1, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 4, 1],
      [1, 1, 1, 1, 1, 1]]

# [110,10],
s2 = [[1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 2, 1, 4, 1],
      [1, 3, 0, 0, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1]]

# [211,12],
s3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 2, 0, 3, 4, 1],
      [1, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1]]

# [300,13],
s4 = [[1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 1, 4],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 2, 1, 0, 0, 0, 0],
      [0, 3, 1, 0, 0, 0, 0]]

# [551,10],
s5 = [[1, 1, 1, 1, 1, 1],
      [1, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 4, 2, 2, 4, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 3, 1, 1, 1],
      [1, 1, 1, 1, 1, 1]]

# [722,12],
s6 = [[1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 4, 1],
      [1, 0, 0, 0, 2, 2, 3, 1],
      [1, 0, 0, 1, 0, 0, 4, 1],
      [1, 1, 1, 1, 1, 1, 1, 1]]

# [1738,50],
s7 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 1, 1, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
      [0, 2, 1, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 1, 4]]

# [1763,22],
s8 = [[1, 1, 1, 1, 1, 1],
      [1, 4, 0, 0, 4, 1],
      [1, 0, 2, 2, 0, 1],
      [1, 2, 0, 1, 0, 1],
      [1, 3, 0, 0, 4, 1],
      [1, 1, 1, 1, 1, 1]]

# [1806,41],
s9 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 0, 0, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 2, 0, 1],
      [1, 0, 1, 0, 0, 1, 2, 0, 1],
      [1, 0, 4, 0, 4, 1, 3, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1]]

# [10082,51],
s10 = [[1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 0, 1, 1, 0],
       [1, 3, 2, 0, 0, 1, 1],
       [1, 1, 0, 2, 0, 0, 1],
       [0, 1, 1, 0, 2, 0, 1],
       [0, 0, 1, 1, 0, 0, 1],
       [0, 0, 0, 1, 1, 4, 1],
       [0, 0, 0, 0, 1, 4, 1],
       [0, 0, 0, 0, 1, 4, 1],
       [0, 0, 0, 0, 1, 1, 1]]

# [16517,48],
s11 = [[1, 1, 1, 1, 1, 1, 1],
       [1, 4, 0, 0, 0, 4, 1],
       [1, 0, 2, 2, 1, 0, 1],
       [1, 0, 2, 0, 1, 3, 1],
       [1, 1, 2, 0, 1, 0, 1],
       [1, 4, 0, 0, 4, 0, 1],
       [1, 1, 1, 1, 1, 1, 1]]

# [22035,38],
s12 = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
       [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
       [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 1, 0, 1, 4, 0, 4, 1],
       [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]

# [26905,28],
s13 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 4, 0, 0, 0, 0, 0, 2, 0, 1],
       [1, 0, 2, 0, 0, 0, 0, 0, 4, 1],
       [1, 0, 3, 0, 0, 0, 0, 0, 2, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 4, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# [41715,53],
s14 = [[0, 0, 1, 0, 0, 0, 0],
       [0, 2, 1, 4, 0, 0, 0],
       [0, 2, 0, 4, 0, 0, 0],
       [3, 2, 1, 1, 1, 0, 0],
       [0, 0, 1, 4, 0, 0, 0]]

# [48695,44],
s15 = [[1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 2, 2, 0, 1],
       [1, 0, 2, 0, 2, 3, 1],
       [1, 4, 4, 1, 1, 1, 1],
       [1, 4, 4, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0]]

# [91344,111],
s16 = [[1, 1, 1, 1, 1, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 0, 0],
       [1, 2, 1, 0, 1, 1, 1, 1],
       [1, 4, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 5, 0, 5, 0, 1],
       [1, 0, 5, 0, 1, 0, 1, 1],
       [1, 1, 1, 0, 3, 0, 1, 0],
       [0, 0, 1, 1, 1, 1, 1, 0]]

# [3301278,76],
# Warning: This problem is very hard and could be impossible to solve without a good heuristic!
s17 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 3, 0, 0, 1, 0, 0, 0, 4, 1],
       [1, 0, 2, 0, 2, 0, 0, 4, 4, 1],
       [1, 0, 2, 2, 2, 1, 1, 4, 4, 1],
       [1, 0, 0, 0, 0, 1, 1, 4, 4, 1],
       [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

# [??,25],
s18 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 4, 1, 0, 0, 0, 0]]

# [??,21],
s19 = [[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0],
       [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 4],
       [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 2, 0, 4, 1, 0, 0, 0]]


# Utility functions for printing states and moves.
# You do not need to understand any of the functions below this point.


# Helper function of prettyMoves
# Detect the move from state s --> s1
def detectDiff(s, s1):
    row, col = getKeeperPosition(s)
    row1, col1 = getKeeperPosition(s1)
    if (row1 == row + 1):
        return 'Down'
    if (row1 == row - 1):
        return 'Up'
    if (col1 == col + 1):
        return 'Right'
    if (col1 == col - 1):
        return 'Left'
    return 'fail'


# Translates a list of states into a list of moves
def prettyMoves(lists):
    initial = 0
    action = []
    for states in (lists):
        if (initial != 0):
            action.append(detectDiff(previous, states))
        initial = 1
        previous = states
    return action


# Print the content of the square to stdout.
def printsquare(v):
    if (v == blank):
        print(' ', end='')
    if (v == wall):
        print('#', end='')
    if (v == box):
        print('$', end='')
    if (v == keeper):
        print('@', end='')
    if (v == star):
        print('.', end='')
    if (v == boxstar):
        print('*', end='')
    if (v == keeperstar):
        print('+', end='')


# Print a state
def printstate(s):
    row = s.shape[0]
    col = s.shape[1]
    for i in range(row):
        for j in range(col):
            printsquare(s[i, j])
        print('\n')


# Print a list of states with delay.
def printlists(lists):
    for states in (lists):
        printstate(states)
        print('\n')


if __name__ == "__main__":
    sokoban(s1, h0)

    sokoban(s2, h0)

    sokoban(s3, h0)

    sokoban(s4, h0)
