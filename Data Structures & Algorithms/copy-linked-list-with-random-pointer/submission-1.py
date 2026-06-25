"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dummy = Node(0)
        tail = dummy 
        hash = {None: None} # original : copy
        while curr:
            new_node= Node(curr.val)
            hash[curr]= new_node
            tail.next= new_node
            tail = tail.next
            curr = curr.next
        curr2= head
        while curr2:
            random_node =curr2.random
            rand_node_copy= hash[random_node]
            curr_copy = hash[curr2]
            curr_copy.random = rand_node_copy
            curr2= curr2.next
        return dummy.next  