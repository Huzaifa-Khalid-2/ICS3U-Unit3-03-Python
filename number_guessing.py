#!/usr/bin/env python3

# Created by: Huzaifa
# Created on: March 2022
# This function takes a random integer between 0-9
# and tells the user if they guessed corretly

import constants_two


def main():
    # this function takes a random integer between 0-9
    # and tells the user if they guessed corretly

    # input
    user_guess = int(input("Insert any number between 0-9 (integers): "))
    # process and output
    print("")
    if user_guess == constants_two.SECRET_NUMBER:
        print("Hooray you guessed correctly !! :)")
    if user_guess != constants_two.SECRET_NUMBER:
        print("Oh No!!! guessed incorrectly :(")

    print("\nDone.")


if __name__ == "__main__":
    main()
