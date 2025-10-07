# Definition for singly-linked list.
import heapq
from typing import List, Optional
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = count()  # Unique sequence count

        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, next(counter), l))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, next(counter), node.next))

        return dummy.next

# Helper function to convert list to ListNode
def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Convert list of lists to list of ListNodes
input_lists = [[2, 6], [1, 4, 5], [1, 3, 4]]
linked_lists = [build_linked_list(l) for l in input_lists]

sol = Solution()
merged_head = sol.mergeKLists(linked_lists)

# Print the merged linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

print_linked_list(merged_head)
