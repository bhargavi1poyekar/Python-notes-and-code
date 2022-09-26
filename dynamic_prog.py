'''
Dynamic programming is technique for solving optimization problem, 
by breaking it down into simpler subproblems, and utilizing the fact that optimal solution 
to overall problems, depend on optimal solution to subproblems.

-we remember problems and answer ans reuse it

-optimization of divide and conquer

-Property of overlapping subproblems:

Approach:
- Top Down with Memoization: solve bigger prob by recursively finding solns to smaller subprobs.
storing theresult of already solved subprobs: Memoization
'''

'''
Fibonacci using Memoization
'''
# def fib(n,memo):
#     if n<=1:
#         return n
#     if n==2:
#         return 1
#     if n not in memo:
#         memo[n]=fib(n-1,memo)+fib(n-2,memo)
#     return memo[n]
# memo=dict()
# print(fib(5,memo))

'''
Approach 2: Tabulation- Bottom Up approach
-avoids recursion
-solves all related subprobs first, and filled in table
-soln to the top is then computed
'''
'''
Fibonacci with tabulation
'''
# def fib(n): 
#     tab=[0,1]
#     for i in range(2,n+1):
#         tab.append(tab[i-1]+tab[i-2])
#     return tab[n-1]
    
# print(fib(6))
        




