class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int currentMax = 0;
        for (int num : nums) {
            if (num == 1) {
                currentMax += 1;
            } else {
                max = Math.max(currentMax,max);
                currentMax = 0;
            }
        }
        max = Math.max(currentMax,max);
        return max;
    }
}