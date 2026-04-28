# Day 16 - Remove Duplicates From Sorted List
# Platform: LeetCode

# Day16.py

# 1. Define the ListNode class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Helper functions
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

# 3. Solution class
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# 4. Run test
if __name__ == "__main__":
    values = [1, 1, 2, 3, 3]
    head = build_linked_list(values)
    print("Original list:")
    print_linked_list(head)

    solution = Solution()
    head = solution.deleteDuplicates(head)

    print("After removing duplicates:")
    print_linked_list(head)
