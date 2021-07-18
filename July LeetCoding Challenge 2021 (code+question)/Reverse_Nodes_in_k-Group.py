'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. k is a positive
integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes,
only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

Constraints:
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next

    def reverse(self, start, end):
        prev, curr = start, start.next
        first = curr
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start.next = prev
        first.next = curr
        return first
