# LeetCode Problems
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

import array as arr
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def index_two_number_add_up_to_target(self, given_array, target):
        if arr.isArray(given_array) == False:
            print("You should provide an array")

        target = 10
        max_length_of_array = len(given_array)
        print("Maximum Length of array is :" + str(max_length_of_array))


        return target


