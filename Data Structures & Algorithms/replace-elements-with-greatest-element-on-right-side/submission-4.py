class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # [2,4,5,3,1,2]
        length = len(arr) # length = 6
        ans = [0]*length # [0,0,0,0,0,0]
        write = length-1 # 5
        ans[write] = -1 # [0,0,0,0,0,-1]
        write -= 1
        
        if length <= 1:
            return ans
        
        while (write>=0):
            ans[write] = max(arr[write+1], ans[write+1])
            write-=1

        
        return ans

        

        

