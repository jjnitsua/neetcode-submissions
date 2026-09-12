class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Pass 1: weave copies in. A -> A' -> B -> B' -> ...
        curr = head
        while curr:
            copy = Node(curr.val, curr.next, None)
            curr.next = copy
            curr = copy.next

        # Pass 2: assign random pointers using the interleaving.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Pass 3: unweave to separate original and copy lists.
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head