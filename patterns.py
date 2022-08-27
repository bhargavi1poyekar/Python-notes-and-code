#1
'''
*
**
***
****
*****
'''
# num=5
# for i in range(num):
#     for j in range(i):
#         print("*",end="")
#     print("\n")

#----------------------------------------------------

#2
'''
     *
    **
   ***
  ****
'''

# num=5
# for i in range(num):
#     for j in range(num):
#         if(j>=num-i-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n")

#-----------------------------------------------------

#3
'''
    *
   * *
  * * *
 * * * * 
* * * * *
'''
# num=5
# for i in range(num):
#     for j in range(num):
#         if(j>=num-i-1):
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print("\n")

#--------------------------------------------------

#4
'''
1
12
123
1234
12345
'''
# num=5
# for i in range(num):
#     for j in range(i+1):
#         print(j+1,end="")
#     print("\n")

#----------------------------------------------------

#5
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
# num=6
# n=1
# for i in range(num):
#     for j in range(i+1):
#         print(n,end="")
#         print(" ",end="")
#         n=n+1
#     print("\n")
#------------------------------------------

#6
'''
A
BB
CCC
DDDD
EEEEE
'''

# num=6
# for i in range(num+1):
#     for j in range(i):
#         print(chr(65+i-1),end="")
#     print("\n")

#------------------------------------------------

#7
'''
A
B C
D E F
G H I J
K L M N O
'''
# num=6
# n=0
# for i in range(num):
#     for j in range(i+1):
#         print(chr(65+n),end="")
#         print(" ",end="")
#         n=n+1
#     print("\n")
#------------------------------------------

#7
'''
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
'''

# num=6
# for i in range(num):
#     k=1
#     for j in range(num):
#         if(j>=num-i-1):
#             print(f'{k} ',end="")
#             k+=1
#         else:
#             print(" ",end="")
        
    
#     print("\n")

#----------------------------------------------------


#8
'''
1
22
333
4444
55555
'''

# num=6
# for i in range(num+1):
#     for j in range(i):
#         print(i,end="")
#     print("\n")

#------------------------------------------------


#9
'''
     1
    123
   12345
  1234567
 123456789
'''

# num=6
# for i in range(num):
#     k=1
#     for j in range(num+i):
#         if(j>=num-i-1):
#             print(f'{k}',end="")
#             k+=1
#         else:
#             print(" ",end="")
        
    
#     print("\n")

#----------------------------------------------------

#10
'''
     1
    123
   12345
  1234567
 123456789
  1234567
   12345
    123
     1
'''

# num=3
# for i in range(num*2-1):
#     k=1
#     if i<num:
#       for j in range(num+i):
#         if(j>=num-i-1):
#             print(f'{k}',end="")
#             k+=1
#         else:
#             print(" ",end="")
#       print("\n")
#     else:
#       for j in range(2*num-i+num-2):
#           if(j>=i-(num-1)):
#             print(f'{k}',end="")
#             k+=1
#           else:
#             print(" ",end="")
#       print("\n") 

#----------------------------------------------------


#11
'''
123456
12345
1234
123
12
1
'''

# num=6

# for i in range(num):
#      for j in range(num-i):
#           print(j+1,end="")
#      print("\n")     

#----------------------------------------------------


#12
'''
666666
55555
4444
333
22
1
'''

# num=6

# for i in range(num):
#      for j in range(num-i):
#           print(num-i,end="")
#      print("\n")     

#----------------------------------------------------

#13

'''
1
01
101
0101
10101
'''
# num=5
# for i in range(num):
#      for j in range(i+1):
#           if (i+j)%2==0:
#                print(1,end="")
#           else:
#                print(0,end="")
#      print("\n")

#-------------------------------------------------

#14
'''
1          1
12        21
123      321
1234    4321
12345  54321
123456654321
'''

# num=4

# for i in range(num):
#      k=1
#      for j in range(2*(num)+1):
#           if j<=i :
#                print(k,end="")
#                k+=1
#           elif j==num:
#                k=i+1
#           elif j>2*(num)-i-1:
#                print(k,end="")
#                k-=1
          
#           else:
               
#                print(" ",end="")
#      print("\n")
                 
#---------------------------------------------

#15

'''
    1
   232
  34543
 4567654
567898765

'''        
# num=5

# for i in range(num):
#      k=i+1
#      for j in range(num+i):
#           if j>=num-i-1:
#                print(k,end="")
#                if j>=num-1:
#                     k-=1
#                else:
#                     k+=1
          
#           else:
#                print(" ",end="")
#      print("\n")

#----------------------------------------------

#16
'''
1       1
 2     2
  3   3
   4 4
    5
   4 4
  3   3
 2     2
1       1
'''

# num=6
# k=1
# for i in range(2*num-1):
#      for j in range(2*num-1):
#           if j==i or j==2*num-i-2:
#                print(k,end="")
               
#           else:
#                print(" ",end="")
#      if i<=num-2:
#           k+=1
#      else:
#           k-=1
#      print("\n") 

#---------------------------------------------

#17
'''
1
12
123
1234
12345
1234
123
12
1
'''

# num=6
# for i in range(2*num-1):
#      k=1
#      if i<num:
#           for j in range(i+1):
#                print(k,end="")
#                k+=1
#      else:
#           for j in range(2*num-i-1):
#                print(k,end="")
#                k+=1
     
#      print("\n")

#--------------------------------------------

#18

'''
123456
12345
1234
123
12
1

1
12
123
1234
12345
123456
'''
# num=6
# for i in range(2*num+1):
#      k=1
#      if i<num:
#           for j in range(num-i):
#                print(k,end="")
#                k+=1
#      if i==num:
#           pass
#      else:
#           for j in range(i-num):
#                print(k,end="")
#                k+=1
     
#      print("\n",end="")

#--------------------------------------------





