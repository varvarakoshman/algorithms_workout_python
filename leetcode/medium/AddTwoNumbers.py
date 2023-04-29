class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 9 - 9 - 9 - 9 - 9 - 9 - 9
# 9 - 9 - 9 - 9
# 8 - 9 - 9 - 9 - 0 - 0 - 0 - 1

# 1 - 2 - 3
# 4 - 5
# 5 - 7 - 3

# 9 - 9 - 9
# 0 - 1
# 9 - 0 - 0 - 1

# 2 - 4 - 3
# 5 - 6 - 4
# 7 - 0 - 8
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        prev = dummy
        remainder = 0
        while l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            curr_sum = value1 + value2 + remainder
            new_node = ListNode(curr_sum % 10)
            remainder = curr_sum // 10
            prev.next = new_node
            prev = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if remainder == 1:
            prev.next = ListNode(1)
        return dummy.next
