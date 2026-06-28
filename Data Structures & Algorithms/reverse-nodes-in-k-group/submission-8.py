# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseNode(self,prev: ListNode, curr : ListNode) -> tuple[ListNode, ListNode]:
        old_next = curr.next
        curr.next = prev
        prev = curr
        curr = old_next
        return prev, curr
    def reverseKGroup(self,head: ListNode, k: int) -> ListNode:
        prev, curr = None, head
        count = 0

        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        else:
            next_list_head = self.reverseKGroup(curr, k)
            prev,curr = next_list_head, head
            count = 0
            while count < k:
                prev, curr = self.reverseNode(prev, curr)
                count += 1
            return prev