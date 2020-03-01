input=[
    66, 68, 30, 86, 75, 88, 29, 51, 22, 36, 
    93, 70, 74, 90, 72, 50, 46, 88, 47, 90, 
    34, 59, 77, 70, 32, 55, 65, 32, 78, 62, 
    34, 48, 97, 15, 18, 49, 23, 51, 23, 99, 
    19, 34, 50, 25, 23, 56, 11, 28, 71, 83, 
    37, 52, 73, 69]

import sys
import time

def matrix_chain_multiplication_R(p,i,j):
    count=sys.maxsize
    if i==j:
        return 0
    for k in range(i,j):
        count = min(count,
           (matrix_chain_multiplication_R(p,i,k)
            + matrix_chain_multiplication_R(p,k+1,j)
            + p[i-1]*p[k]*p[j])
        )
    return count
    

def execute_R(n):
    print(f'n={n}')
    # print(f'input {input[:n]}')
    
    start=time.time()
    result=matrix_chain_multiplication_R(input[:n],1,n-1)
    end = time.time()
    print(f'Result: {result} Time for R: {end-start}')

execute_R(10)
execute_R(12)
execute_R(15)
execute_R(20)