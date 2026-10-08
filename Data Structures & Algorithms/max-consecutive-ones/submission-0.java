class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int current_max = 0;
        for (int num : nums) {
            if (num == 1) {
                current_max += 1;
            } else {
                if (current_max > max) {
                    max = current_max;
                }
                current_max = 0;
            }
        }
        if (current_max > max) {
            max = current_max;
        }

        return max;
    }
}