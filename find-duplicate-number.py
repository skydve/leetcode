# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

def findDuplicate(nums):
    return int((sum(nums)- sum(set(nums)))/(len(nums) - len(set(nums))))

def findDuplicate2(nums):
    """tortoise and hare algorythm"""
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
        
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1
    

print(findDuplicate2([1, 2, 2, 2, 4]))