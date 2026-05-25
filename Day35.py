# Day 35 - Intersection of Two Linked Lists
# Platform: LeetCode

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        # Traverse both lists until they meet or both reach None
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # Intersection node or None

def build_lists():
    # Shared part: 8 -> 4 -> 5
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    c1.next = c2
    c2.next = c3

    # List A: 4 -> 1 -> 8 -> 4 -> 5
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = c1

    # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    return a1, b1

if __name__ == "__main__":
    headA, headB = build_lists()
    sol = Solution()
    intersection = sol.getIntersectionNode(headA, headB)
    if intersection:
        print("Intersected at:", intersection.val)
    else:
        print("No intersection")

