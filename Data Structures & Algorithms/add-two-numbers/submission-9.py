# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2= l1,l2
        dummy = ListNode(0)
        result = dummy
        trailing= 0
        while (num1 or num2):
            sum = (num1.val if num1 else 0) + (num2.val if num2 else 0) + trailing
            trailing = sum // 10 
            print(sum, trailing)
            digit = ListNode(sum % 10)
            result.next = digit
            result = result.next
            if num1:
                num1= num1.next
            if num2:
                num2= num2.next

        if trailing !=0:
            final_node = ListNode(trailing)
            result.next = final_node
            result = result.next 
        return dummy.next