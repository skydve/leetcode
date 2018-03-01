# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array.

def find_numbers(nums):
    a = set(nums)
    out = []
    for i in range(1, len(nums)+1):
        if i not in a:
            out.append(i)
    return out
