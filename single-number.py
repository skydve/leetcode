# Given an array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    return sum(list(set(nums)))*2 - sum(nums)
