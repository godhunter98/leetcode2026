# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> list[int] | None:
        list_len = 0
        curr = head
        while curr:
            list_len+=1
            curr=curr.next

        curr=head
        for _ in range(list_len//2):
            if curr is not None:
                curr = curr.next
        return curr