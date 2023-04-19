# Name: Utkarsh Lal
# UID: 905792162
# CS 161 Hw 2

#Problem 1
def BFS(TREE):
    #BFS should be approached like an algorithm which returns the nodes left to right according to the increasing depth of the TREE
    # this means that the nodes at the least depth comes first in the search algoritm (left to right in same depth)
    if isinstance(TREE, float) or isinstance(TREE, int) or isinstance(TREE, str): #base case to return floats and strings
        return (TREE,)
    
    searched = []

    q = [TREE] #this is just making a list out of the tuple 
    while q:
        #we  first pop the first element in the array which in the first case is the entire tuple
        #but later the else condition allows seperating the non-tuple elements in the TREE as a list element which allows us to pop it independently
        visiting = q.pop(0)

        if isinstance(visiting, float) or isinstance(visiting, int) or isinstance(visiting, str):
            searched.append(visiting)   #since we always go left to right in the TREE it can be directly added to the result array without any additional filtering

        else:
            q += list(visiting)  #if the element is a tuple, we add the tuple as a list to the end of q to furhter traverse the list and find next elements in BFS
    return tuple(searched)  #finally returning the tuple form which is expected 


#print(BFS(("R", ("I", ("G", ("H", "T"))))))
# print(BFS(((("L", "E"), "F"), "T")))
# print(BFS("root"))


#Problem 2
def DFS(TREE):
    #the concept of DFS involves going to the deepest depth and returning values as we proceed left to right
    #so basically the task is to go to full depth of the first element of the tuple and traceback from there
    if isinstance(TREE, float) or isinstance(TREE, int) or isinstance(TREE, str): #base case to return floats and strings
        return (TREE,)
    
    searched = []
    q = [TREE]
    #the logic is identical to BFS, the only difference comes in the last else statement
    while q:
        visiting = q.pop(0)

        if isinstance(visiting, float) or isinstance(visiting, int) or isinstance(visiting, str):
            searched.append(visiting)
        else:
            q = list(visiting) + q 
            #notice here we are maintaining the order of traversal of a TREE 
            #so the first element remains in that place if it is a tuple instead of pushing it into the back like in case of BFS

    return tuple(searched)

# print(DFS(("A", (("C", (("E",), "D")), "B"))))
# print(DFS(((("A", ("B",)), ("C",), "D"))))


#Problem 3
def DFID_HELPER(visiting, q, i):
    for j in visiting[::-1]:
        q.insert(i,j)

def DFID(TREE, D):
    #the concept right-to-left depth-first iterative-deepening search can be modified from the logic of DFS in the prev 
    #problem. Over here we, instead of popping the firt element, we pop all the element right to left in array and print it in a 
    # resultant array. If we bump into a tuple we break it into a list and append it in its location in the array without changing
    #the configuration of the TREE. 
    if isinstance(TREE, float) or isinstance(TREE, int) or isinstance(TREE, str): #base case to return floats and strings
        return (TREE,)
    
    searched = []
    
    q = [TREE]
    #the logic is identical to BFS, the only difference comes in the last else statement
    while D >= 0:
        for i in range(len(q)-1,-1,-1):
            visiting = q.pop(i)  #going from behind as right to left

            if isinstance(visiting, float) or isinstance(visiting, int) or isinstance(visiting, str):
                searched.append(visiting)
                q.insert(i,visiting)   #we have to maintain the position of that element as this is a deepening search
            else:
                DFID_HELPER(visiting, q,i)  #insert the tuple turned list into the same location in q
        D -= 1 #D denotes the depth of the tree we are . Depth = D(initial value in parameter) - D(current value)

    return tuple(searched)




# print(DFID(((("L", "E"), "F"), "T"), 3))
# print(DFID(((("A", ("B",)), ("C",), "D")), 3))
#assert(DFID(("A", (("C", (("E",), "D")), "B")), 5)) == ('A', 'B', 'A', 'B', 'C', 'A', 'B', 'D', 'C', 'A', 'B', 'D', 'E', 'C', 'A')





#Problem 4

# (homer, baby, dog, poison), where each variable is True if the respective entity is on the west side of the river, and False if it is on the east side.
def FINAL_STATE(S):
    return S == (True,True,True,True) #just checking a particular case

def NEXT_STATE(S, A):
    # (homer, baby, dog, poison)
    return_arr = []
    if A == "h": #homer ony
        homer = not S[0]
        return_arr = [(homer,S[1],S[2],S[3])]
    elif A == "b":
        homer = not S[0]
        baby = not S[1]
        if homer == baby:  #to check that both can move together?
            return_arr = [(homer,baby,S[2],S[3])]
    elif A == "d":
        homer = not S[0]
        dog = not S[2]
        if homer == dog: #homer and dog at same place?
            return_arr = [(homer,S[1],dog,S[3])]
    elif A == "p":
        homer = not S[0]
        poison = not S[3]
        if homer == poison: #homer and poison at same place
            return_arr = [(homer,S[1],S[2],poison)]

    else:
        return []
    
    if return_arr == []:
        return [] #if no change
    
    #the dog and baby, or poisoin and baby are left unsupervised on one side of the river, return [] for invalid state
    if return_arr[0][1] == return_arr[0][2]:
        if return_arr[0][1] != return_arr[0][0] and return_arr[0][1] != return_arr[0][3]:
            return []
    if return_arr[0][1] == return_arr[0][3]:
        if return_arr[0][1] != return_arr[0][0] and return_arr[0][1] != return_arr[0][2]:
            return []
    
    return return_arr
    

def SUCC_FN(S):
    if len(S) == 0:
        return []
    possible_moves = []   #resulatant array for all possible ways to move
    if NEXT_STATE(S,"h") != []:
        possible_moves.append(NEXT_STATE(S,"h")[0])
    if NEXT_STATE(S,"b") != []:
        possible_moves.append(NEXT_STATE(S,"b")[0])
    if NEXT_STATE(S,"d") != []:
        possible_moves.append(NEXT_STATE(S,"d")[0])
    if NEXT_STATE(S,"p") != []:
        possible_moves.append(NEXT_STATE(S,"p")[0])
    
    return possible_moves

def ON_PATH(S, STATES):
    return S in STATES #just checking in the list

def MULT_DFS(STATES, PATH):
    
    for i in STATES:
        x = DFS_SOL(i,PATH)
        if len(x) > 0:  #to check if its not equal to an empty list 
            return x
    return []


def DFS_SOL(S, PATH):
    if FINAL_STATE(S):
        return PATH + [S]  #final result implying a possible path exists
    if ON_PATH(S,PATH):
        return []    #negating repetative case
    return MULT_DFS(SUCC_FN(S),PATH + [S])  #recursing back to MULT_DFS to check for all possible ways to move in the path

# print(SUCC_FN((False, False, True, True)))
#assert(DFS_SOL((False, False, False, False), [])) == [(False, False, False, False), (True, True, False, False), (False, True, False, False), (True, True, True, False), (False, False, True, False), (True, False, True, True), (False, False, True, True), (True, True, True, True)]
# print(SUCC_FN((True,False,True,True)))



