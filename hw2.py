# Name: Utkarsh Lal
# UID: 905792162
# CS 161 Hw 2

#Problem 1
def BFS(tree):
    #BFS should be approached like an algorithm which returns the nodes left to right according to the increasing depth of the tree
    # this means that the nodes at the least depth comes first in the search algoritm (left to right in same depth)
    searched = []

    q = [tree] #this is just making a list out of the tuple 
    while q:
        #we  first pop the first element in the array which in the first case is the entire tuple
        #but later the else condition allows seperating the non-tuple elements in the tree as a list element which allows us to pop it independently
        visiting = q.pop(0)

        if isinstance(visiting, float) or isinstance(visiting, int) or isinstance(visiting, str):
            searched.append(visiting)   #since we always go left to right in the tree it can be directly added to the result array without any additional filtering

        else:
            q += list(visiting)  #if the element is a tuple, we add the tuple as a list to the end of q to furhter traverse the list and find next elements in BFS
    return tuple(searched)  #finally returning the tuple form which is expected 


print(BFS(("R", ("I", ("G", ("H", "T"))))))


#Problem 2
def DFS(tree):
    
