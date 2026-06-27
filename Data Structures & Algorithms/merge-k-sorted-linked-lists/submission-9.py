# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2ll(self, list1: Optional[ListNode], list2: Optional[ListNode]):
       #estan ordendas localmente
        head1, head2 =list1, list2
        dummy = ListNode(0)
        res = dummy
        while head1 and head2:
            if head1.val < head2.val:
                res.next = head1
                head1 = head1.next
            else:
                res.next = head2
                head2= head2.next
            res = res.next
        if head1:
            res.next = head1
        else:
            res.next = head2
        return dummy.next
    def mergeRecu(self, lists, left, right) -> Optional[ListNode]:
        # el caso base seria cuando tenemos solo dos ll a mergear
        if left == right:
            return lists[left]
        mid =(left + right) //2
        leftList = self.mergeRecu(lists, left, mid)
        rightList = self.mergeRecu(lists, mid+1, right)
        return self.merge2ll(leftList, rightList)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeRecu(lists, 0, len(lists)-1)