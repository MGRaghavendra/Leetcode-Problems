class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            if head.val==val:
                head=head.next
                prev=head
                current=current.next
            elif current.val==val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        return head