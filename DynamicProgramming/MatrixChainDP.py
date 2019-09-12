import sys, time
gk = lambda i,j: str(i) + ', ' + str(j)
MAX = sys.maxsize

def matrix_chain_order_dp(p,m):
    n = len(p) - 1
    for i in range(1,n+1):
        for j in range(i,n+1):
            m[gk(i,j)] = MAX
    return lookup_chain(m,p,1,n)

def lookup_chain(m,p,i,j):
    if m[gk(i,j)] < MAX:
        return m[gk(i,j)]
    if i == j:
        m[gk(i,j)] = 0
    else:
        for k in range(i,j):
            q = lookup_chain(m,p,i,k) + lookup_chain(m,p,k+1,j) + (p[i-1]*p[k]*p[j])
            if q < m[gk(i,j)]:
                m[gk(i,j)] = q
    "print(m)"
    return m[gk(i,j)]

p = [30,35,15,5,10,20,25]
m = {}
print(matrix_chain_order_dp(p,m))
print(m)
