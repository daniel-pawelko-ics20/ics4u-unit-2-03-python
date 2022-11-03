#!/usr/bin/env python3

# Created on: Oct-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# This class creates an integer stack

from math import isnan


class MrCoxallStack:
    # create the stack as a List
    stack_as_list = []

    def push(self, pushed_number: int):
        if isnan(pushed_number):
            print("Number not passed")
        else:
            # add a number ot the list
            self.stack_as_list.append(pushed_number)

    def get_stack(self):
        # return stack
        return self.stack_as_list

    def pop_stack(self):
        if (self.stack_as_list) == 0:
            # Stack has no elements
            return "Stack has a length of 0"
        else:
            # Pop stack and return it
            return self.stack_as_list.pop()

    def peek_stack(self):
        if len(self.stack_as_list) == 0:
            # Stack has no elements
            return "Stack has a length of 0"
        else:
            # Return last element in array
            return self.stack_as_list[-1]
