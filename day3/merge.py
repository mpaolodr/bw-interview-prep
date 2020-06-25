# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        Questions:
        Will both list have the same length?
        """

        # set pointer for both llist
        pa = l1
        pb = l2

        # initialize new list and its pointer
        new_list = None
        pn = None

        # loop through each list until one of pointer is None
        while pa is not None and pb is not None:

            # we compare values so new llist will be sorted
            if pa.val < pb.val:

                # set node as head of new list
                if new_list is None:

                    new_list = pa

                    # move pointer of new list to head of list
                    pn = new_list

                else:

                    # we set node where pa is pointing as the next node in new list
                    pn.next = pa

                    # we move pointer of new llist to new node
                    pn = pn.next

                # move pa to next node in list
                pa = pa.next

            else:

                if new_list is None:

                    new_list = pb
                    pn = new_list

                else:

                    pn.next = pb
                    pn = pn.next

                pb = pb.next

        # once we get here, either pa or pb is pointing at None
        if pa is None:

            # we loop through remaining nodes in pb and add them to new llist
            while pb is not None:

                if new_list is None:

                    new_list = pb
                    pn = new_list

                else:

                    pn.next = pb
                    pn = pn.next

                pb = pb.next

        elif pb is None:

            while pa is not None:

                if new_list is None:
                    new_list = pa
                    pn = new_list

                else:
                    pn.next = pa
                    pn = pn.next

                pa = pa.next

        # if both lists are None, meaning we're given empty linked lists
        elif pa is None and pb is None:
            return None

        return new_list
