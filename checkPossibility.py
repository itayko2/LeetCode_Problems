# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        def check(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                arr1 = nums[:i] + nums[i+1:]
                arr2 = nums[:i+1] + nums[i+2:]
                return check(arr1) or check(arr2)
            
        return True
