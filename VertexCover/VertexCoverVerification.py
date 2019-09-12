import sys
import copy
import collections

"""
This code is for the following tasks in
Part 2: Vertex Cover – Reduction and Verification:

Task II
Task III.I


"""

def main():
    gfilename = sys.argv[1]
    cfilename = sys.argv[2]
    k = int(sys.argv[3])

    graph = load_graph(gfilename)
    candidates = load_candidates(cfilename)

    """
    Your code here. (You can add your own helper functions elsewhere)
    This code should output "yes"/"no" for each candidate if it's a vertex cover of size k.
    (i.e. If there are 5 candidates, print 5 "yes"/"no", seperated by new lines)
    """

    # remove edges from a copy of the graph
    for vc in candidates:
        if len(vc) != k:
            print("no")
            continue
        copy = graph.copy()
        for vertex in vc:
            copy[vertex].clear()
            for x in range(len(copy)):
                if vertex in copy[x]:
                    copy[x].remove(vertex)

        # check if the candidate removed all the edges
        printYes = True
        for v in copy:
            if len(copy[v]) != 0:
                print("no")
                printYes = False
                break
        if printYes:
            print("yes")








def load_candidates(filename):
    candidates = []
    adj_list = collections.defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            candidates.append([int(v) for v in line.strip().split()])
    return candidates


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
