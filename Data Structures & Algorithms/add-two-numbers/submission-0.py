# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        cnt = 0
        while l1 != None:
            num1 += (l1.val) * 10 **cnt
            l1 = l1.next
            cnt += 1

        num2 = 0
        cnt2 = 0
        while l2 != None:
            num2 += (l2.val) * 10 **cnt2
            l2 = l2.next
            cnt2 += 1

        sum = num1 + num2

        head = ListNode(sum%10)
        curr = head
        sum //= 10
        while sum:
            curr.next = ListNode(sum%10)
            curr = curr.next
            sum //= 10

        return head

        