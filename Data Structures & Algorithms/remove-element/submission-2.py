class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        def _swap(a, b, nums):
            temp = nums[b]
            nums[b] = nums[a]
            nums[a] = temp
            return nums

        k = 0
        write = scout = 0
        # [3,2,2,3]
        # val = 3
        while (scout<=len(nums)-1):
            if nums[scout] != val:
                k+=1
                nums = _swap(write, scout, nums)
                scout+=1
                write+=1
            else:
                # assuming write is at the same pos
                scout+=1
        return k
