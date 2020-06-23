# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # grab combined values of each linked list
        num1 = self.reverse_num(l1)
        num2 = self.reverse_num(l2)

        # loop through each element of string value of sum of two linked lists
        result = [num for num in str(num1 + num2)]

        # create new linked list
        head = None

        # loop through each value and make new Node with integer as value
        for num in result:

            # if no item is linked list, item will be new head
            if head is None:

                head = ListNode(int(num))

            # current head will be set as the next node of current element
            else:

                cur_head = head
                head = ListNode(int(num))
                head.next = cur_head

        return head

    def reverse_num(self, node):

        # container for each value of linked list
        reversed = []

        # joined value of nodes
        reversed_num = ""

        # set cur to head of linked list
        cur = node

        # loop through linked list and append to reversed
        while cur is not None:
            reversed.insert(0, cur.val)

            # set next node to be cur
            cur = cur.next

        # concatenate each element
        for num in reversed:
            reversed_num += str(num)

        # return concatenated string and convert to integer
        return int(reversed_num)
