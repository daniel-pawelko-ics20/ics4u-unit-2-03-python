#!/usr/bin/env python3

# Created on: Oct-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# This program uses the MrCoxallStack

from mr_coxall_stack import MrCoxallStack


def main():
    # this function uses the MrCoxallStack
    my_new_stack = MrCoxallStack()

    try:
        some_number = int(input("Enter and integer: "))

        print("Calling push method: ")
        my_new_stack.push(some_number)
        print(my_new_stack.get_stack())

        print("\nCalling pop method: ")
        print(my_new_stack.pop_stack())

        print("\nCalling peek method: ")
        print(my_new_stack.peek_stack())
    except Exception as e:
        print("Input Invalid :(")
        print(e)

    print("\nDone.")


if __name__ == "__main__":
    main()
