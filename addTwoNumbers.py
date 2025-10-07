# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        current = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_int(node):
    digits = []
    while node:
        digits.append(str(node.val))
        node = node.next
    # Since digits are reversed, reverse to get the actual number string
    digits.reverse()
    return int("".join(digits))

l1 = list_to_linkedlist([2,4,3])
l2 = list_to_linkedlist([5,6,4])

solution = Solution()
result_node = solution.addTwoNumbers(l1, l2)

number = linkedlist_to_int(result_node)
print(number)  # This will print: 807
