# Greedy Algorithms

'''
Activity Selection Problem
'''
# activities=[["A1",0,6],
#             ["A2",3,4],
#             ["A3",1,2],
#             ["A4",5,8],
#             ["A5",5,7],
#             ["A6",8,9]]

# def activity(activities):
#     activities.sort(key=lambda x:x[2])# -> O(NlogN) 
#     i=0
#     firstAct=activities[i][0]
#     print(firstAct)
    
#     for j in range(len(activities)): # -> O(N)
#         if activities[j][1]>activities[i][2]:
#             print(activities[j][0])
#             i=j
    
# activity(activities)

'''
Coin Change Problem
'''

# def coinChange(totalNumber, coins):
    
#     coins.sort(reverse=True)
#     i=0
#     count=0
#     while totalNumber!=0: # -> O(N)
#         if coins[i]<=totalNumber:
#             print(coins[i])
#             totalNumber-=coins[i]
#             count+=1
#         else:
#             i+=1
    
#     return count

# print(coinChange(35,[1,2,5,10,20,50,100]))

'''
Fractional Knapsack Problem
'''
# class Item:
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value
#         self.ratio = value / weight

# def knapsackMethod(items, capacity):
#     items.sort(key=lambda x: x.ratio, reverse = True)
#     usedCapacity = 0
#     totalValue = 0
#     for i in items:
#         if usedCapacity + i.weight <= capacity:
#             usedCapacity += i.weight
#             totalValue += i.value
#         else:
#             unusedWeight = capacity - usedCapacity
#             value = i.ratio * unusedWeight
#             usedCapacity += unusedWeight
#             totalValue += value
        
#         if usedCapacity == capacity:
#             break
#     print("Total value obtained: "+str(totalValue))

# item1 = Item(20,100)
# item2 = Item(30,120)
# item3 = Item(10,60)
# cList = [item1, item2, item3]

# knapsackMethod(cList, 50)

'''
Best time to Buy and Sell Stocks
'''

# def maxProfit(self, prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
    
#     i=0
#     j=1
#     max_profit=0
    
#     while j<len(prices):
        
#         if prices[i]<=prices[j]:
#             max_profit=max(max_profit,prices[j]-prices[i])
#         else:
#             i=j
#         j+=1
    
#     return max_profit



    