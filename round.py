#!/usr/bin/env python3

# Created by: Rohnin. B
# Created on: Sep 2021
# this program rounds a float to the users inputted number


def rounder(user_number_float, user_round_by_int):
    # this function rounds a float to the users inputted number

    # process
    rounded_number = (user_number_float[0] * (10 ** user_round_by_int)) + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number / (10 ** user_round_by_int)

    user_number_float[0] = rounded_number


def main():
    # this function gets number_to_round and Rround_by_int
    user_number_list_int = []

    # input
    user_number_string = input("Enter the number you'd like to round: ")
    user_round_by_string = input("Enter the decimal place you'd like to round to: ")

    try:
        user_number_float = float(user_number_string)
        user_number_list_int.append(user_number_float)
        user_round_by_int = int(user_round_by_string)
        # function call
        rounder(user_number_list_int, user_round_by_int)
        if user_round_by_int < 0:
            print("\nMake sure the number you're rounding by is positive.")
        else:
           print("\nThe rounded number is {}.".format(user_number_list_int[0]))
    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
