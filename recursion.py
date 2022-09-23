'''
Fibonacci numbers
'''

# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1)+fib(n-2)

# print(fib(6))

'''
Factorial
'''

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(4))

'''
Sum of digits
'''

# def sum_dig(n):
#     if n==0:
#         return 0
#     return n%10 + sum_dig(n//10)

# print(sum_dig(1453))

'''
Power of Number
'''
# def power(base,pow):
#     if pow==0:
#         return 1
#     return base*power(base,pow-1)

# print(power(4,3))

'''
GCD
'''

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# print(gcd(48,18))

'''
Decimal to Binary
'''

# def dec_bin(n):
#     if n==0:
#         return n
#     return n%2 + 10*dec_bin(n//2)

# print(dec_bin(13))

'''
Product of array
'''

# def productOfArray(arr):
#     if len(arr)==1:
#         return arr[0]
#     return arr[0]*productOfArray(arr[1:])

'''
Recursive Range
'''
# def recursiveRange(num):
#     if num==1:
#         return 1
#     return num+recursiveRange(num-1)

'''
Reverse string
'''

# def reverse(strng):
#     if len(strng)==2:
#         return strng[1]+strng[0]
#     else:
#         return strng[len(strng)-1]+reverse(strng[:len(strng)-1])

'''
Is Palindrome
'''
# def isPalindrome(strng):
#     if len(strng)==0:
#         return True
#     if strng[0]!=strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

'''
Flatten Array
'''

# def flatten(arr):
#     result=[]
#     for item in arr:
#         if type(item) is list:
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result

'''
Capitalize First:

capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']
'''
# def capitalizeFirst(arr):
#     ans=[]
#     if len(arr)==0:
#         return ans
#     ans.append(arr[0][0].upper()+arr[0][1:])
#     return ans + capitalizeFirst(arr[1:])

'''
Capitalize Words
'''
# def capitalizeWords(arr):
#     # TODO
    
#     ans=[]
#     if len(arr)==0:
#         return ans
#     ans.append(arr[0].upper())
#     return ans+capitalizeWords(arr[1:])

