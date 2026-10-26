# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptr = head
        for _ in range(n-1):
            ptr = ptr.next

        head_t = head
        temp = None
        while(ptr.next != None):
            temp = head_t
            head_t = head_t.next
            ptr = ptr.next

        if temp:
            temp.next = head_t.next
            return head
        else:
            if head_t == head:
                return head_t.next
            return None


        