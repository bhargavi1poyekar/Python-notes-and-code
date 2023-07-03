'''
1047. Remove All Adjacent Duplicates In String
'''
# def removeDuplicates(self, s: str) -> str:

#         stack=[]

#         for i in s:
#             if not stack:
#                 stack.append(i)
#             else:
#                 if stack[-1]==i:
#                     stack.pop()
#                 else:
#                     stack.append(i)
        
#         return(''.join(stack))

'''
844. Backspace String Compare
'''

# def backspaceCompare(self, s: str, t: str) -> bool:

#         stack1=[]
#         stack2=[]
#         for i in s:
#             # print(stack1)
#             if i=='#' and stack1:
#                 stack1.pop()
#             elif i!='#':
#                 stack1.append(i)

        
#         for i in t:
#             # print(stack2)
#             if i=='#' and stack2:
#                 stack2.pop()
#             elif i!='#':
#                 stack2.append(i)
        
#         return stack1==stack2
        

'''
1566. Make The String Great
'''

# def makeGood(self, s: str) -> str:
#         stack=[]

#         for i in s:
#             if stack and i!=stack[-1] and i.lower()==stack[-1].lower():
#                 stack.pop()
#             else:
#                 stack.append(i)
        
#         return(''.join(stack))