'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

'''

def twoSum(arr, target):
    d ={}
    for x in range(len(arr)):
        d[arr[x]] = x 
    for x in range(len(arr)):
        if target-arr[x] in d:
            return [ d[arr[x]], d[target-arr[x]] ]  

print(twoSum([2, 7, 11, 15], 9))