import sys
import collections
import networkx as nx


"""
This code is for the following tasks in
Part 2: Vertex Cover Reduction and Verification

Task I
Task III.2


"""

def main():
    filename = sys.argv[1]
    k = int(sys.argv[2])
    G = load_graph(filename)
    n = len(G)
    graph = nx.Graph()

    """

    This code should print  "yes"/"no" if there's a vertex cover of size k.
    (As long as there's a vertex cover of size k, print "yes"
     Note that this code prints only one "yes" or "no")

    Also, the code should write the complement graph of the input to a .txt file.
    You can write the graph to .txt with this command:
    write_graph("complement.graph", YOUR_complement GRAPH)


    This code should use the "reduction from clique" idea to come up with
    the answer.

    You can find cliques with this command:   nx.find_cliques(graph)
    """

    for node in G:
        graph.add_node(node)
    for node in G:
        for edge in G[node]:
            graph.add_edge(node, edge)

    # 1. Let 'comp' be the complement of graph
    comp = complement(graph)

    # 2. k' = |V| - k
    k_comp = graph.number_of_nodes() - k

    # 3. return CLIQUE(comp, k_comp)
    cliques = nx.find_cliques(comp)
    printNo = True
    for clique in cliques:
        if len(clique) == k_comp:
            print("yes")
            printNo = False
            break
    if printNo:
        print("no")

    write_graph("complement.graph.txt", comp)


def complement(graph):
    comp = nx.Graph()
    for node in graph:
        comp.add_node(node)
    for u in graph:
        for v in graph:
            if v not in graph[u] and u != v:
                comp.add_edge(u,v)
    return comp

#def reduction(comp, k):



def write_graph(filename, adj_list):
    with open(filename, "w") as fout:
        for u in adj_list:
            for v in adj_list[u]:
                if u < v:
                    fout.write(str(u)+" "+str(v)+"\n")


def load_graph(filename):
    adj_list = collections.defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            u, v = [int(v) for v in line.strip().split()]
            adj_list[u].add(v)
            adj_list[v].add(u)
    return adj_list


if __name__ == "__main__":
    main()
