input=[
    66, 68, 30, 86, 75, 88, 29, 51, 22, 36, 
    93, 70, 74, 90, 72, 50, 46, 88, 47, 90, 
    34, 59, 77, 70, 32, 55, 65, 32, 78, 62, 
    34, 48, 97, 15, 18, 49, 23, 51, 23, 99, 
    19, 34, 50, 25, 23, 56, 11, 28, 71, 83, 
    37, 52, 73, 69]

import sys
import time

def matrix_chain_multiplication_S(p):
    # Sequential algorithm with nested for-loops

    n=len(p)
    m = [[0 for x in range(n)] for y in range(n)]

    for i in range(1,n):
        m[i][i]=0
    for l in range(2,n): #l is the chain length
        for i in range(1, n-l+1):
            j=i+l-1
            m[i][j]=sys.maxsize
            for k in range(i, j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j]=q

    return m[1][n-1]

def execute_S(n):
    print(f'n={n}')

    start=time.time()
    result=matrix_chain_multiplication_S(input[:n])
    end = time.time()
    print(f'Result: {result} Time for S: {end-start}')

execute_S(10)
execute_S(12)
execute_S(15)
execute_S(20)
execute_S(30)
execute_S(50)