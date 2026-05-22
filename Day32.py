# Day 32 - Linked list cycle
# Platform: LeetCode

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

head1 = create_linked_list_with_cycle([3,2,0,-4], 1)
head2 = create_linked_list_with_cycle([1,2], 0)
head3 = create_linked_list_with_cycle([1], -1)

solution = Solution()
print(solution.hasCycle(head1))  # Output: True
print(solution.hasCycle(head2))  # Output: True
print(solution.hasCycle(head3))  # Output: False
