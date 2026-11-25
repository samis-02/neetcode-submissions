class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        running_count = 0
        for num in nums:
            if num == 1: 
                running_count+=1
                if running_count > max_count : 
                    max_count = running_count
            else : 
                running_count = 0
            
        return max_count