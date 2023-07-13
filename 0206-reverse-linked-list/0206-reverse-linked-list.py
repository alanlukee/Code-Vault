# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        newList =None
        current = head
        while current:
            newNode = current.next
            current.next = newList
            newList = current
            current = newNode
        return newList
