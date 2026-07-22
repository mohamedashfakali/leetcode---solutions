class Solution:

    def reverseLL(self, node):

        prev = None
        curr = node

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def isPalindrome(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        slow = self.reverseLL(slow)

        fast = head

        while slow:

            if fast.val != slow.val:
                return False

            slow = slow.next
            fast = fast.next

        return True