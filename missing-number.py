# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

def missingNumber(nums):
    return sum(range(1, len(nums)+1)) - sum(nums)

print(missingNumber([3, 0, 1]))