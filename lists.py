# Temp above avg
# n_days=int(input("How many days temp?: "))
# temp=[]
# for i in range(n_days):
#     temp.append(int(input(f'Day {1} high temp: ')))

# avg_tmp=sum(temp)/len(temp)
# print(f"Avg temp:{avg_tmp}")
# count_abv_avg=0
# for i in range(n_days):
#     if temp[i]>avg_tmp:
#         count_abv_avg+=1
        
# print(f'{count_abv_avg} day(s) above avg')

'''
Missing Number'''

# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# sum_100=int(100*(100+1)/2)

# sum_list=sum(list1)

# missing=sum_100-sum_list

# print(missing)

'''
Two sum (find all pairs)'''

# input_l=[1,2,3,2,3,4,5,6]
# target=6

# seen=[]
# pairs=[]

# for i in range(len(input_l)):
#     if target-input_l[i] in seen and target-input_l[i]!=input_l[i]:
#         pairs.append([target-input_l[i],input_l[i]])
#     else:
#         seen.append(input_l[i])

# print(pairs)

'''
Find max product of 2 integers in array with all positive values'''

# max_prod=0
# list1=[1,20,30,5,6,7,31,30,56,2,3,5,34]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if i==j:
#             continue
#         if list1[i]*list1[j]>max_prod:
#             max_prod=list1[i]*list1[j]

# print(max_prod)

'''
Unique Elements
'''
# list1=[1,2,3,4,5,1,6,7]
# check_list=[]

# for i in list1:
#     if i in check_list:
#         print(f"{i} is duplicate")
#         exit
#     else:
#         check_list.append(i)

'''
Rotate matrix
'''
# import numpy as np
# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)
# n=len(matrix)

# # for 0 in range(n//2):
# first=0
# last=n-0-1
# for i in range(first, last):
#     # get top left
#     top=matrix[0][i]
#     # move left bottom to top left 
#     matrix[0][i]=matrix[-i-1][0]
#     # move right bottom to left bottom
#     matrix[-i-1][0]=matrix[-0-1][-i-1]
#     #move right top to bottom right
#     matrix[-0-1][-i-1]=matrix[i][-0-1]
#     #move top to top right
#     matrix[i][-0-1]=top

# print(matrix)

'''
Best Score
'''

# givenList=[84,85,86,87,85,90,85,83,23,45,84,1,2,0]

'''
method 1
'''
# list_set=list(set(givenList))
# list_set.sort(reverse=1)
# print(list_set)

# print(list_set[0],list_set[1])


'''
method 2
'''
# a = givenList   #make a copy

# a.sort(reverse=True)

# first = a[0]

# second = None

# for element in givenList:

#     if element != first:

#         second = element

#         print(first, second)
#         break
    

'''
Duplicate Number
'''
# myList=[1, 1, 2, 2, 3, 4, 5]
# new_list=[]
 
# for i in myList:

#     if i not in new_list:

#         new_list.append(i)

# print(new_list)

'''
Dictionary Excercise 
'''
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

'''
STACK
'''



