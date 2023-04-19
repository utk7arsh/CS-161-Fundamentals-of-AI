# Name: Utkarsh Lal
# UID: 905792162
# CS 161 Hw 1


#Problem 1
def PAD(N):

    #base case of 0,1,2 as given in the question
    if N in [0,1,2]:
        return 1
    
    #Since PAD(n+1) = PAD(n-1) + PAD(n-2) it can be made to PAD(n) = PAD(n-2) + PAD(n-3) given n >= 3
    else:
        return PAD(N-2) + PAD(N-3) #solved recursively


#Problem 2
def SUMS(N):
    #base case is that we do 0 additions
    if N in [0,1,2]:
        return 0
    
    #when breaking any PAD to find no of additions we have to find how every part of the PAD breaking returns to the base case
    # when we have all the base case sum condition then the sums is equal to number of times we break the function into 2 parts
    # SUMS(3) = SUMS(1) + SUMS(0) so 1 addition because broke 1 time
    # SUMS(5) = SUMS(2) + SUMS(3) = SUMS(2)  + SUMS(1) + SUMS(0) so 2 additions for 2 breaks
    else:
        return 1 + SUMS(N-2) + SUMS(N-3)  #recursively solved


#Problem 3
def ANON(TREE):

    #expecting that only possible elements of the TREE (nodes) are floats or strings
    if type(TREE) == float or type(TREE) == int or type(TREE) == str:
        return "?"   #replacing every node with ?
    
    else:
        return tuple([ANON(t) for t in TREE]) # type change to retain tuple property



#Problem 4
def TREE_HEIGHT(TREE):
    #for counting the height we have to look at the tuples inside each element of the base tuple
    #basically (1, ("FOO", 3.1), -0.2) means the height is 2 as the element ("FOO", 3.1) is a forming a seperate branch at a new level
    children = [TREE_HEIGHT(child) for child in TREE if isinstance(child, tuple)]
    if children:
        return 1 + max(children)
    else:
        return 1



#Problem 5
def TREE_ORDER(TREE):
    #since we are given that the tree is a ordered tuple we can define branching of the tree to three parts
    #In a postorder traversal of a tree of three nodes - we go to left, right and then middle
    
    if isinstance(TREE, float) or isinstance(TREE, int) or isinstance(TREE, str): #base case to return floats and strings
        return (TREE,)
    
    else:
        left_child, middle_child, right_child = TREE  #based on the defination of ordered tree
        return TREE_ORDER(left_child) + TREE_ORDER(right_child) + (middle_child,) #recursively traverse the child in postorder


#Test cases 
# assert(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100)))) == (3, 10, 7, 16, 20, 18, 100, 30, 15)
# assert(TREE_ORDER(((1, 2, 3), 7, 8))) == (1, 3, 2, 8, 7)
# assert(TREE_ORDER(((1, 2, 3), 8, (4, 5 ,7)))) == (1, 3, 2, 4, 7, 5, 8) 
# print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))) 
# print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))
# assert(TREE_HEIGHT(("R", ("I", ("G", ("H", "T")))))) == 4
# assert(TREE_HEIGHT(("A", ("B", ("C", 1.2, 3), "D", ("E", 4.5)), ("F", 6.7)))) == 3
# assert(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))) == ((('?', '?'), ('?', '?')), ('?', '?'))

# network = []
# for i in range(0,13):
#     network.append(PAD(i))
# assert(network == [1,1,1,2,2,3,4,5,7,9,12,16,21])

# assert(SUMS(5)) == 2
# assert(SUMS(7)) == 4
    