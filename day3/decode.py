

# get a list of the multipliers in order
def get_k(s):

    # will contain numbers in string form
    # if number is more than 1 digit, it will concatenate first before pushing to list
    temp_s = ""

    # will contain string form of digits and whitespaces
    temp_list = []

    # we filter the whitespaces and only return the numbers
    final_list = []

    # check element in string if number or not
    for i in range(len(s)):

        # if number, we add to string
        if s[i].isdigit() == True:

            temp_s += s[i]

        # if not a number, we append to temp_list and reset the temp_s for next numbers
        elif s[i].isdigit() == False:
            temp_list.append(temp_s)
            temp_s = ""

    # we loop and convert strings to numbers
    for index in range(len(temp_list)):

        try:

            # if character can't be converted to number, we ignore
            new_char = int(temp_list[index])
            final_list.append(new_char)

        except ValueError:

            continue

    return final_list


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # to check if string provided is empty, return empty string
        if s != "":

            # get all multipliers in order
            list_of_k = get_k(s)

            # get index of opening and closing brackets
            b_tracker = Stack()
            b_pos = []

            # to see if we need to evaluate anythin
            # if this is  empty, meaning no multipliers, we return string
            if len(list_of_k) == 0:
                return s

            # we check the index of each pair of opening and closing brackets
            # we'll use this to evaluate what's inside the brackets
            for index in range(len(s)):

                # if opening, we put index in stack
                if s[index] == "[":

                    b_tracker.push(index)

                # if closing, we grab the last opening from stack and store as tuples
                elif s[index] == "]":

                    opening = b_tracker.pop()

                    b_pos.insert(0, (opening, index))

            # sort the tuples based on first value
            new_pos = sorted(b_pos, key=lambda item:  item[0])

            # loop through each tuple, whatever's inside the pair needs to be evaluated
            for i in range(len(new_pos)):

                # word to multiply
                to_evaluate = s[new_pos[i][0] + 1: new_pos[i][1]]

                # word with brackets
                word = s[new_pos[i][0]: new_pos[i][1] + 1]

                # multiplier in string form and words with bracket
                # so we can target it in string and we replace
                phrase_to_replace = str(list_of_k[i]) + word

                # new string after evaluating and replacing
                new_word = s.replace(
                    phrase_to_replace, list_of_k[i] * to_evaluate)

                # if there're brackets in new word, we call the function again passing the new_word

                if "[" in new_word:

                    return self.decodeString(new_word)

                # base case
                else:

                    return new_word

        else:

            return ""


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, x):
        self.storage.append(x)

    def pop(self):

        value = self.storage.pop()

        return value
