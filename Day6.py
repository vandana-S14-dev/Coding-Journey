# Day 6 - Merge Two Sorted List
# Platform: LeetCode

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

# Helper function to convert Python list to linked list
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# Helper function to convert linked list back to Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
if __name__ == "__main__":
    # Example 1
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = Solution().mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4]

    # Example 2
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    merged = Solution().mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: []

    # Example 3
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    merged = Solution().mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: [0]
