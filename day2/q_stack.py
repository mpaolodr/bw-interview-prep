class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # we'll use 2 stacks to do the FIFO for used by Queue
        # first stack will be the main storage
        # second one will be used when removing the first element
        self.storage = Stack()
        self.temp_storage = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # add values to end of storage
        self.storage.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # we store in variables to make it readable
        stg = self.storage
        tmp = self.temp_storage

        # we move values from storage to temp and we remove the last element in temp
        while stg.is_empty() is False:

            tmp_val = stg.pop()
            tmp.push(tmp_val)

        # last element in temp which is the first element in main storage
        removed_val = tmp.pop()

        # we put back all elements in temp to main storage
        while tmp.is_empty() is False:

            stg_val = tmp.pop()
            stg.push(stg_val)

        # removed value
        return removed_val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        stg = self.storage

        # we grab element at index 0
        if stg.is_empty() is not True:

            return stg.storage[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        return self.storage.is_empty()


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):

        # this will add values to end of the list
        self.storage.append(value)

    def pop(self):

        # we store the value thaat was removed so we can return it later and improve readability
        removed_value = self.storage.pop()

        return removed_value

    def is_empty(self):

        if len(self.storage) == 0:

            return True

        else:

            return False
