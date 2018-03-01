# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

from collections import Counter

def majorityElement(nums):
    return Counter(nums).most_common(1)[0][0]

def majorityElement2(nums):
    nums.sort()
    return nums[len(nums)//2]

print(majorityElement2(['A', 'b', 'b']))