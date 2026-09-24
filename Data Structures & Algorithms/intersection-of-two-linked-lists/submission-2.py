# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        aSet = []
        bSet = []

        currA = headA
        currB = headB

        while currA:
            aSet.append(currA)
            currA = currA.next
        
        while currB:
            bSet.append(currB)
            currB = currB.next
        
        for node in aSet:
            if node in bSet:
                return node
        
        return None