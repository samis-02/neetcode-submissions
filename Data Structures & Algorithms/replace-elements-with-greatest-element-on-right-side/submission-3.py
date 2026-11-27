class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # [2,4,5,3,1,2]
        length = len(arr) # length = 6
        ans = [0]*length # [0,0,0,0,0,0]
        write = 0

        def _find_running_max(i, arr):
        # invariant running_max -> at every step, running_max holds the largest of the numbers to the right of write poa (scout is passed which is right+1)
            running_max = -1
            while (i <= length-1):
                running_max = max(arr[i], running_max)
                i+=1
            return running_max
        

        if length <=1 :
            ans[0] = -1
            return ans
        
        while (write < length-1):
            scout = write+1 # scout = 1
            ans[write] = _find_running_max(scout, arr)
            write+=1
        
        ans[-1] = -1
        return ans

