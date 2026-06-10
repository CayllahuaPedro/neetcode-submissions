# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ''' primero hallamos el nodo del medio con un algo de t
        tortuga y liebre'''
        middle = None
        slow, fast = head, head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        middle = slow
        ''' luego tenemos que revertir la 2da mita'''
        nprev, nhead =None,  middle.next
        middle.next= None
        while nhead:
            temp = nhead.next
            nhead.next = nprev
            nprev = nhead
            nhead = temp
        rhead = nprev

        ''' ahora tenemos que hacer un merge de estas dos
        listas'''
        # print("===")
        while rhead:
            # print("head: ", head.val)
            next_node = head.next # guardamos el prox
            next_rnode = rhead.next
            # print("r head a append: ", rhead.val)
            head.next = rhead # le metemos en n- k
            head = head.next # avanzamos a ese rev_i
            # print("append r head: ",head.val )
            head.next = next_node #le enchufamos el nodo sig original
            if head.next:
                head = head.next # avanzamos de nuevo
            rhead = next_rnode # avanzamos el reversed l list
            # print("newHead: ", head.val)
            # print("===")
