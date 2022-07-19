# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        target = head
        while target != None:
            counter += 1
            target = target.next
        if counter % 2 == 0:
            half = counter / 2
            half = int(half)
        else:
            half = int(counter / 2)
        export = head
        for item in range(0, half):
            export = export.next
        return export