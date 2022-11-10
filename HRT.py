# def sum_cond(self,x, y, carry):
#         if x==0 and y==0 and carry==0:
#             return (0,0)
#         elif (x==0 and y==1 and carry==0) or (x==1 and y==0 and carry==0):
#             return(1,0)
#         elif x==1 and y==1 and carry==0:
#             return(0,1) 
#         elif x==0 and y==0 and carry==1:
#             return (1,0)
#         elif (x==0 and y==1 and carry==1) or (x==1 and y==0 and carry==1):
#             return(0,1)
#         elif x==1 and y==1 and carry==1:
#             return(1,1) 
        
# def addBinary(self, a: str, b: str) -> str:
    
#     addition=[]
    
#     if len(a)>len(b):
#         b=b.zfill(len(a))
#     elif len(a)<len(b):
#         a=a.zfill(len(b))
    
#     a=a[::-1]
#     b=b[::-1]
    
#     carry=0
    
#     print(a,b)
#     for i in range(len(a)):
#         add, carry=self.sum_cond(int(a[i]),int(b[i]), carry)
#         addition.append(str(add))
    
    
#     if carry==1:
#         addition.append(str(carry))
    
#     return ''.join(addition[::-1])

# # Method 2

# carry = 0
# result = ''

# a = list(a)
# b = list(b)

# while a or b or carry:
#     if a:
#         carry += int(a.pop())
#     if b:
#         carry += int(b.pop())

#     result += str(carry %2)
#     carry //= 2

# return result[::-1]

# '''
# Q2
# '''

# def solution(queryType, query):
#     ans = 0
#     hmap = {}
#     ck = 0
#     cv = 0
#     for i in range(len(queryType)):
#         cmd = queryType[i]
#         quer = query[i]
#         if cmd == "insert":
#             key,val = quer[0],quer[1]
#             hmap[key-ck]=val-cv
#         elif cmd == "addToValue":
#             k = quer[0]
#             cv+=k
#         elif cmd == "addToKey":
#             k = quer[0]
#             ck+=k
#         else:
#             k = quer[0]
#             k-=ck
#             val = hmap[k] + cv
#             ans = ans + val
#     print(hmap)
#     return ans


# queryType=['insert','insert','addToValue','addToKey','insert','get']
# query=[[1,2],[2,3],[2],[1],[1,2],[2]]

# print(solution(queryType,query))

class Tracker():
    def allocate(hostType):
        
        
    def deallocate(hostType):
        
    
    def solution(queries):
        tracker=Tracker()
        ans=[]
        for query in queries:
            task=query.split(' ')
            if task[0]=='A':
                ans.append(tracker.allocate(task[1]))
            if task[0]=='D':
                tracker.deallocate(task[1])
        return ans