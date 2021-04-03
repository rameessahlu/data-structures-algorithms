import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        length = -1
        while temp != None:
            length +=1
            temp = temp.next
        result = 0
        while head != None:
            if head.val ==1 :
                result += int(math.pow(2,length))
            length -= 1
            head = head.next
        return result