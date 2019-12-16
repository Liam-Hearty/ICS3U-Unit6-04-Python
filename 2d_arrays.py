#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program uses a 2D array

import random


def avg_of_numbers(passed_in_2D_list, rows, columns):
    # This function finds the average up all the elements in a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
    total = total / (rows + columns)

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    try:
        rows = int(input("How many rows would you like: "))
        columns = int(input("How many columns would you like: "))
    except(ValueError):
        print("Please input a number.")

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    average = avg_of_numbers(a_2d_list, rows, columns)
    print("The average of all the numbers is: {0} ".format(average))


if __name__ == "__main__":
    main()
