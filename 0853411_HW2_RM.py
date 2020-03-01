input=[
    66, 68, 30, 86, 75, 88, 29, 51, 22, 36, 
    93, 70, 74, 90, 72, 50, 46, 88, 47, 90, 
    34, 59, 77, 70, 32, 55, 65, 32, 78, 62, 
    34, 48, 97, 15, 18, 49, 23, 51, 23, 99, 
    19, 34, 50, 25, 23, 56, 11, 28, 71, 83, 
    37, 52, 73, 69]

import sys
import time

def lookup_chain(m,p,i,j):
    # print(f'i {i} j {j}')
    # print(f'm[i][j]= {m[i][j]}')
    if m[i][j] < sys.maxsize:
        # print(f'm[i][j] < sys.maxsize, m[i][j]={m[i][j]}')
        # already calculated
        return m[i][j]
    if i==j:
        m[i][j]=0
        # print(f'i==j, m[i][j]={m[i][j]}')
    else:
        for k in range(i,j):
            # print(f'p[i-1]*p[k]*p[j] {p[i-1]*p[k]*p[j]}')
            q=(lookup_chain(m,p,i,k)
            +lookup_chain(m,p,k+1,j)
            +p[i-1]*p[k]*p[j])
            # print(f'q {q} m[i][j] {m[i][j]}')
            if q < m[i][j]:
                m[i][j]=q
    # print(f'm {m}')
    return m[i][j]
            
def matrix_chain_multiplication_RM(p):
    # memoization
    n=len(p)
    Matrix = [[0 for x in range(n)] for y in range(n)] 
    for i in range(0,n):
        for j in range(i,n):
            Matrix[i][j]=sys.maxsize
    # print(f'Matrix {Matrix}')
    return lookup_chain(Matrix,p,1,n-1)


def execute_RM(n):
    print(f'n={n}')

    start=time.time()
    result=matrix_chain_multiplication_RM(input[:n])
    end = time.time()
    print(f'Result: {result} Time for RM: {end-start}')

execute_RM(10)
execute_RM(12)
execute_RM(15)
execute_RM(20)
execute_RM(30)
execute_RM(50)