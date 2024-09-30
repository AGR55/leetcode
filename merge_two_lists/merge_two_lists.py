# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer: Optional[ListNode]
        merge_list: ListNode
        merge_list = list1 if list1.value < list2.value else list2
        while list1.next is not None or list2.next is not None:
            if list1.value < list2.value:
                
