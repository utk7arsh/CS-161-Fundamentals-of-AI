############## 
# Name: Utkarsh Lal
# UID: 905792162
# Homework 4 #
##############

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets Color c" when there are k possible colors
def node2var(n, c, k):
    print(n)
    return (n - 1) * k + c #as given in page 2 of spec - var index

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"
def at_least_one_color(n, k):
    l = []
    for i in range(1,k+1):
        l.append(node2var(n, i, k))     # adds variables (from node) of a (single) clause to the list 
    return l

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"
def at_most_one_color(n, k):
    cl = []
    for i in range(1, k + 1): #valid till k
        for j in range(1, i):
            cl.append([- node2var(n, i, k), - node2var(n, j, k)])  #de morgan's law A ∧ B = ¬A v ¬B , A v B = ¬A ∧ ¬B
                                                                   #so we append the negatives of variables here
    return cl

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"
def generate_node_clauses(n, k):
    clause_net = at_most_one_color(n, k)
    clause_net.append(at_least_one_color(n, k))
    return clause_net #basically clauses is the culmination of all possible node clauses which can be found using the two 
                    #helper functions used above and contactinating them

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e (represented by a list)
# cannot have the same color"
def generate_edge_clauses(e, k):
    # we are required to return the nodes connected to the edges
    a,b = e
    clause = []
    for i in range(1, k + 1):
        clause.append([-node2var(a, i, k), -node2var(b, i, k)])
    return clause

# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            print("n",n)
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count




# Example function call
if __name__ == "__main__":
   graph_coloring_to_sat('./graph2.txt', "graph2_8colors.cnf", 8)

