'''
707. Design Linked List
'''

# class ListNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class MyLinkedList:

#     def __init__(self):
#         self.size=0
#         self.head=None

#     def get(self, index: int) -> int:
#         if index<0 or index>=self.size:
#            return -1
#         curr=self.head
#         for i in range(index):
#             curr=curr.next
        
#         return curr.val

#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0,val)
        

#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size,val)

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index>self.size:
#             return

#         curr=self.head
#         newnode=ListNode(val)
        
#         if index<=0:
#             newnode.next=curr
#             self.head=newnode
#         else:
#             for i in range(index-1):
#                 curr=curr.next
#             newnode.next=curr.next
#             curr.next=newnode
        
#         self.size+=1

#     def deleteAtIndex(self, index: int) -> None:
        
#         if index<0 or index>=self.size:return

#         curr=self.head
#         if index==0:
#             self.head=self.head.next
#         else:
#             for i in range(index-1):
#                 curr=curr.next
#             curr.next=curr.next.next
        
#         self.size-=1

'''
206. Reverse Linked List
'''
# def reverseList(head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
    
#     prev=next=None
#     curr=head
    
#     while curr:
        
#         next=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next
    
#     head=prev
#     return head
        
'''
141. Detect a cycle in Linked List- Floyd's Cycle Algo
'''
# def hasCycle(self, head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
    
#     slow=fast=head
    
#     while slow and slow.next and fast.next and fast.next.next:
#         slow=slow.next
#         fast=fast.next.next
#         if slow==fast:
#             return True
#     return False

'''
876. Middle Of a Linked List
'''

# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         fast=head
#         slow=head

#         while fast and fast.next:
#             fast=fast.next.next
#             slow=slow.next
        
#         return slow

'''83. Linked List Remove Duplicates'''

# def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
#         slow=head
#         fast=head

#         while(fast):
#             # print(slow.val, fast)
#             if fast.val!=slow.val:
#                 slow.next=fast
#                 slow=fast
#             fast=fast.next
        
#         if slow!=None:
#             slow.next=None
#         return head

        # ptr=head

        # while(ptr and ptr.next):
        
        # if ptr==ptr.next:
        #     ptr.next=ptr.next.next
        # else:
        #     ptr=ptr.next
        
        # return head

'''
24. Swap Nodes in pair
'''

# def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         if not head or not head.next:
#             return head
#         dummy=head.next

#         while(head and head.next):

#             next_n=head.next.next
#             head.next.next=head

#             if next_n and next_n.next:
#                 head.next=next_n.next
#             else:
#                 head.next=next_n
#             head=next_n
        
#         return dummy

'''
2130. Maximum Twin Sum of a Linked List
'''
# def pairSum(self, head: Optional[ListNode]) -> int:

#         slow,fast=head,head
        

#         # Find middle of linked list
#         while(fast and fast.next):
#             prev=slow
#             slow=slow.next
#             fast=fast.next.next
        
#         prev,curr=None,slow

#         while(curr):
#             next_node=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next_node

#         start=head
#         max_sum=0
#         while(prev):
#             max_sum=max(max_sum, start.val+prev.val)
#             prev=prev.next
#             start=start.next
        
#         return max_sum

'''
234. Palindrome Linked List
'''

#  def isPalindrome(self, head: Optional[ListNode]) -> bool:

#         fast,slow=head,head

#         while(fast and fast.next):
#             slow=slow.next
#             fast=fast.next.next
        
#         prev,curr=None,slow

#         while(curr):
#             nn=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nn
        
#         while(prev):
#             if prev.val!=head.val:
#                 return False
#             prev=prev.next
#             head=head.next

#         return True

'''
2074. Reverse Nodes in Even Length Groups.
'''

# if not head or not head.next:
#             return head

#         prev=head
#         curr=head.next

#         grp_count=2
#         count=0
#         count_ptr=head.next
#         node_count=0
#         while curr:

#             while(count_ptr and node_count<grp_count):
#                 count_ptr=count_ptr.next
#                 node_count+=1
                
#             if node_count%2==0:
#                 con,tail=prev,curr
#                 while(count<grp_count and curr):
#                     nn=curr.next
#                     curr.next=prev
#                     prev=curr
#                     curr=nn
#                     count+=1
                    
#                 con.next=prev
#                 tail.next=curr
#                 prev=tail
#                 count=0
            
#             else:
#                 curr=count_ptr
#                 while(prev.next!=curr):
#                     prev=prev.next
#             node_count=0
#             grp_count+=1
            
        
#         return(head)

'''
2095. Delete the Middle Node of a Linked List
'''

# def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         if not head or not head.next:
#             return None

#         # prev=None
#         slow=head
#         fast=head.next.next

#         while(fast and fast.next):

#             # prev=slow
#             slow=slow.next
#             fast=fast.next.next
        
#         # if slow:prev.next=slow.next 
#         # else: prev.next=None
#         if slow.next:
#             slow.next=slow.next.next

#         return(head)

'''
203. Remove Linked List Elements
'''
# def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

#         if not head: return head

#         dummy=ListNode(0)
#         dummy.next=head
        
#         prev,curr=dummy,head

#         while(curr):
#             if curr.val==val:
#                 prev.next=curr.next
#             else:
#                 prev=curr
#             curr=curr.next
        
#         return dummy.next

'''
1721. Swapping nodes in a linked list
'''

# def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         beg=head
#         end=head
        
#         count=1
#         while(count<k):
#             beg=beg.next
#             count+=1
        
#         fast=beg
#         while(fast.next):
#             fast=fast.next
#             end=end.next
        
#         beg.val,end.val=end.val,beg.val
#         return head

'''
237. Delete node in linked list
'''

# def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """

#         node.val=node.next.val
#         node.next=node.next.next

'''
445. Add 2 numbers 2
'''
# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#         l1=self.reverseList(l1)
#         l2=self.reverseList(l2)
        
#         dummy=ListNode()
#         curr=dummy
#         carry=0

#         while l1 or l2 or carry:

#             val1=l1.val if l1 else 0
#             val2=l2.val if l2 else 0

#             val=val1+val2+carry
#             carry=val//10
#             val=val%10

#             newNode=ListNode(val)
#             curr.next=newNode
#             curr=curr.next

#             l1=l1.next if l1 else 0
#             l2=l2.next if l2 else 0
        
#         return self.reverseList(dummy.next)
    
#     def reverseList(self,head):

#         prev=None
#         curr=head
#         while(curr):
#             nn=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nn
        
#         return prev

'''
142. Linked List Cycle 2.
'''

# def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         slow=head
#         fast=head

#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next

#             if (slow==fast):
#                 slow=head

#                 while(slow!=fast):
#                     slow=slow.next
#                     fast=fast.next

#                 return fast

'''
725. Split Linked List in Parts
'''
# def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

#         curr=head
#         node_count=0
#         while(curr):
#             curr=curr.next
#             node_count+=1
        
#         each_part_count=node_count//k
#         node_with_extra=node_count%k

#         ans=[]
#         for i in range(1,k+1):
#             h=curr=ListNode()
#             prev=None
#             count=0

#             if i<=node_with_extra:
#                 while(count<each_part_count+1):
#                     prev=curr
#                     curr.next=head
#                     curr,head=curr.next,head.next
#                     count+=1
#                 prev.next.next=None
#             else:
#                 print(curr)
#                 while(count<each_part_count):
#                     prev=curr
#                     curr.next=head
#                     curr,head=curr.next,head.next
#                     count+=1
#                 if prev: prev.next.next=None
               
#             ans.append(h.next)
#             count=0
#         return ans

'''
2181. Merge Nodes in Between Zeros
'''
# def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         head=head.next
#         start,curr=head,head

#         while(curr):
#             sum=0
#             while(curr.val!=0):
#                 sum+=curr.val
#                 curr=curr.next
#             start.val=sum
#             start.next=curr.next
#             curr=curr.next
#             start=curr
        
#         return head