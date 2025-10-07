#Definition for singly-linked list.
#from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # Calculate the sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10

            # Create a new node with the digit and link it to the result list
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in l1 and l2
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next


# Helper to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to convert linked list to integer
def linkedlist_to_int(node):
    digits = []
    while node:
        digits.append(str(node.val))
        node = node.next
    return int("".join(digits[::-1]))

# Test case
l1 = list_to_linkedlist([2, 4, 3])  # 342
l2 = list_to_linkedlist([5, 6, 4])  # 465

solution = Solution()
result_node = solution.addTwoNumbers(l1, l2)
number = linkedlist_to_int(result_node)
print(number)  # Output: 807 (342 + 465)
