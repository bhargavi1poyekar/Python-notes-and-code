'''
1.1 is Unique
'''

# def isUnique(str):
#     hash_tab={}
#     for i in str:
#         if i in hash_tab:
#             return False
#         else:
#             hash_tab[i]=1
#     return True

# print(isUnique('hb6 27=j'))

''' If we cannot use additional space: If we are allowed to modify the input string, we could sort the string in O(n log(n)) time and then
linearly check the string for neighboring characters that are identical. Careful, though: many sorting
algorithms take up extra space.

'''

#1.2 Check permutation: Given two strings, write a method to decide if one is a permutation of the 
# other. 

# Questions:

# 1. Case sensitive??
# 2. WHitespace??

# Both should be of same length

# 1. Solution 1: Sort both strings and compare
# def check_perm(str1,str2):

#     if len(str1)!=len(str2):
#         return False
    
#     str1=sorted(str1)
#     str2=sorted(str2)
#     if str1==str2:
#         return True
#     else:
#         return False
    
# 2. Solution 2:
# from collections import Counter

# def check_perm(str1,str2):

#     if len(str1)!=len(str2):
#         return False

#     counter=Counter()

#     for i in str1:
#         counter[i]+=1
    
#     for i in str2:
#         if counter[i]==0:
#             return False
#         counter[i]-=1
    
#     return True

# print(check_perm('2314', '1234'))

#1.3 Urlify

# def urlify(str,true_len):

#     space_count=0
#     for i in range(true_len):
#         if str[i]==" ":
#             space_count+=1
    
#     index=true_len+space_count*2
#     for i in range(true_len-1,-1,-1):
#         if str[i]==" ":
#             str[index-3:index]="%20"
#             index-=3
#         else:
#             str[index-1]=str[i]
#             index-=1
        
#     return ''.join(str)

# print(urlify(list("Mr John SMith    "),13))

#1.4 Palindrome Permutation: Find if any permutation of string is a palindrome

#  Odd length string: only one character with odd count, else even counts
# Even length str: all even counts

# def palin_perm(str):

#     str=str.replace(' ','')
#     count_tab={}
#     for i in str:
#         if i.lower() in count_tab:
#             count_tab[i.lower()]+=1
#         else:
#             count_tab[i.lower()]=1
#     print(count_tab)
#     odd=0
#     for i in count_tab:
#         if count_tab[i]%2==1:
#             if odd:
#                 return False
#             odd=1
#     return True

# print(palin_perm('Random Words'))

'''
1.6 String Compression
'''

# def str_compr(string):

#     n=len(string)
#     ptr1=0
#     ptr2=0
#     new_str=[]
#     while(ptr2<=n-1):

#         if string[ptr2]!=string[ptr1]:
#             new_str.append(string[ptr1])
#             new_str.append(str(ptr2-ptr1))
#             ptr1=ptr2
#         ptr2+=1
#     new_str.append(string[ptr1])
#     new_str.append(str(ptr2-ptr1))
#     return ''.join(new_str)

# print(str_compr('aabcccccaaa'))


# def compress(chars): 

   
#     n=len(chars)

#     if n==1:
#         return 1
    
#     ptr1=0
#     ptr2=1
#     index=0
#     count=1
#     while(ptr2<n):
#         if chars[ptr1]!=chars[ptr2]:
#             chars[index]=chars[ptr1]
#             index+=1
#             if count>1 and count<10:
#                 chars[index]=str(count)
#                 index+=1
#             elif count>=10:
#                 chars[index:index+len(str(count))]=str(count)
#                 index+=len(str(count))
#             count=0
#             ptr1=ptr2
#         count+=1
#         ptr2+=1
    
#     chars[index]=chars[ptr1]
#     index+=1
#     if count>1 and count<10:
#         chars[index]=str(count)
#         index+=1
#     elif count>=10:
        
#         chars[index:index+len(str(count))]=str(count)
#         index+=len(str(count))
#     count=1
    
#     return index

# chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(chars[:compress(chars)])

'''
1.5 One Away
'''

# def check_replace(str1,str2):
#     flag=0
#     for i in range(len(str1)):
#         if str1[i]!=str2[i] and flag!=1:
#             flag=1
#         elif str1[i]!=str2[i] and flag==1:
#             return False
#     return True

# def check_remove_insert(str1,str2):

#     flag=0
#     st1_ptr=0
#     st2_ptr=0

#     while(st1_ptr<len(str1) and st2_ptr<len(str2)):
#         if str1[st1_ptr]!=str2[st2_ptr] and flag!=1:
#             flag=1
#             st1_ptr+=1
#         elif str1[st1_ptr]!=str2[st2_ptr] and flag==1:
#             return False
#         elif str1[st1_ptr]==str2[st2_ptr]:
#             st1_ptr+=1
#             st2_ptr+=1
        
#     return True

# def one_away(str1,str2):

#     if len(str1)==len(str2):
#         return check_replace(str1,str2)
#     elif len(str1)-len(str2)==1:
#         return check_remove_insert(str1,str2)
#     elif len(str2)-len(str1)==1:
#         return check_remove_insert(str2,str1)

#     return False
        
# str1='palks'
# str2='pal'
# print(one_away(str1,str2))

'''
1.8 Zero Matrix
'''

# def zero_matrix(arr):
    
#     rows=[]
#     cols=[]

#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j]==0:
#                 rows.append(i)
#                 cols.append(j)

#     for row in rows:
#         for i in range(len(arr[0])):
#             arr[row][i]=0
        
#     for col in cols:
#         for j in range(len(arr)):
#             arr[j][col]=0

#     return arr 
# print(zero_matrix([
#             [1, 2, 3, 4, 0],
#             [6, 0, 8, 9, 10],
#             [11, 12, 13, 14, 15],
#             [16, 0, 18, 19, 20],
#             [21, 22, 23, 24, 25]
#         ]))


'''
1.9 String Rotation
'''

# Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring 
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one 
# call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat").

# So, we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2. Regardless of 
# where the division between x and y is, we can see thatyx will always be a substring of xyxy.That is, s2 will 
# always be a substring of s1s1. 

# def string_rotation(str1,str2):
#     if len(str1)==len(str2) and len(str1)>0:
#         return str2 in str1+str1 
#     return False
# print(string_rotation('waterbottle','erbottlewat'))