s = [[0,1,1,3,3,3],[0,0,2,3,3,3],[0,0,0,3,3,3],[0,0,0,0,4,5],[0,0,0,0,0,5]]
def print_optimal_parens(s,i,j):
    if i == j:
        print("A" + str(i+1))
    else:
        print(" (")
        print_optimal_parens(s,i,s[i][j] - 1)
        print_optimal_parens(s,s[i][j],j)
        print(") ")
print(print_optimal_parens(s,0,5))
