class Solution {
    
    // public int removeElement(int[] nums, int val) {
    //     int k = 0;
    //     for (int i=0; i<nums.length; i++){
    //         if (nums[i] != val){
    //             nums[k] = nums[i+1];
    //             k++;
    //         }
    //     }
    //     return k;
    // }

    public int removeElement(int[] nums, int val) {
        int i = 0;
        int j = nums.length-1;

        while (i<=j){
            if (nums[i] == val){
                nums[i] = nums[j];
                j--;
            }
            else{
                i++;     
            }
        }
        return i;
    }

    
}