# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        merge = list1 + list2
        merge.sort()
        return merge

list1 = [1,2,4]
list2 = [1,3,4]
sol = Solution()
print(sol.mergeTwoLists(list1, list2))

