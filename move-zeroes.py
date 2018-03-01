# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

nums = [0, 1, 0, 3, 12]

def moveZeros(nums):
    filtered = list(filter(lambda x: x!=0, nums))
    nums[:] = filtered + [0 for _ in range(len(nums)-len(filtered))]

def moveZeros2(nums):
    zeros = 0
    for num in nums:
        if num == 0:
            nums.remove(0)
            zeros += 1
    nums += [0 for _ in range(zeros)]

def moveZeros3(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    
    
moveZeros3(nums)
print(nums)