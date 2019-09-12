import sys
import random
import collections
import time

"""
This code is Part 1:Vertex Cover - Approximation
"""


def main():
    filename = sys.argv[1]
    algo = sys.argv[2]
    G = load_graph(filename)

    cover = []
    if algo == "greedy-vertex":
        cover = greedy_vertex(G)
    elif algo == "greedy-edge":
        cover = greedy_edge(G)
    else:
        print "Incorrect arguments"
        exit()

    output_cover(cover)


def output_cover(cover):
    with open("approxOutput.txt", "w") as fout:
        for v in cover:
            fout.write(str(v)+"\n")


def greedy_edge(adj_list):
    """
    Implement your code for greedy edge here.
    It should return a list of vertices that covers every edge.
    """
    start_time = time.time()
    # C = 0
    cover = []
    # While |E| > 0
    while len(adj_list) > 0:
        # Select an edge {u,v} in E
        for u in range(len(adj_list)):
            if len(adj_list[u]) > 0:
                v = next(iter(adj_list[u]))
                # C = C U {u,v}
                if u not in cover:
                    cover.append(u)
                if v not in cover:
                    cover.append(v)
                # Remove any edges incident to u or v in E
                for x in range(len(adj_list)):
                    if u in adj_list[x]:
                        adj_list[x].remove(u)
                    if v in adj_list[x]:
                        adj_list[x].remove(v)
            if u in adj_list:
                adj_list.pop(u)
            if v in adj_list:
                adj_list.pop(v)
        # Check if all edges have been consumed
        end = True
        for z in adj_list:
            if len(adj_list[z]) > 0:
                end = False
                break
        if end == True:
            break
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    return cover


def greedy_vertex(adj_list):
    """
    Implement your code for greedy vertex here.
    It should return a list of vertices that covers every edge.
    """
    start_time = time.time()
    # C = 0
    cover = []
    # While |E| > 0
    while len(adj_list) > 0:
        # Select the highest degree vertex v in G
        max = 0
        for v in range(len(adj_list)):
            if len(adj_list[v]) > max:
                max = len(adj_list[v])
                toAdd = v
        # C = C U {v}
        if toAdd in cover:
            break
        cover.append(toAdd)
        # Remove v and all adjacent edges from G
        for v in adj_list:
            try:
                adj_list[v].remove(toAdd)
            except:
                pass
        adj_list.pop(toAdd)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    return cover



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
