# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# from optparse import Values  # Not needed, remove this line
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        values = []

        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()

        # Build new sorted linked list
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


lists = [
    build_linked_list([1, 4, 5]),
    build_linked_list([1, 3, 4]),
    build_linked_list([2, 6]),
]

sol = Solution()
merged_head = sol.mergeKLists(lists)

print_linked_list(merged_head)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
