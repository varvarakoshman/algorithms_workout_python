# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    slow_pointer = fast_pointer = head
    count = 1
    while fast_pointer.next.next is not None:
        if count >= k:
            slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
        count += 1
    if k > count:
        head.value = head.next.value
    slow_pointer.next = slow_pointer.next.next

# k >= 2
#
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> _6_ -> 7 -> 8 -> 9
# k = 4

# 0 -> 1
# k = 2
# 1