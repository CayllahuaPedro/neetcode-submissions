# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev, curr = dummy, dummy
        prev.next = head
        for _ in range(n):
            curr= curr.next
        ''' ahora el curr esta en el found - 1 nodo'''
        ''' en caso de que con solo correr el curr ya haya alcanzado el 
        tope en ese caso; el curr.next ya no existe'''

        while curr.next:
            curr = curr.next 
            prev = prev.next

        found = prev.next 
        nextFound= found.next
        print(found.val)
        if prev.val==0 and not nextFound:
            #quire decir que tanto el prev como el siguiente son
            #nulos aka: devolvemos lista vacia
            return None
        if not nextFound:
            #quire decir que el found es el ultimo de la lista
            prev.next = None
        else:
            print(prev.val, nextFound.val)
            prev.next = nextFound
        return dummy.next