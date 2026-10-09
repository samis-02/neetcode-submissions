class Solution {
    public int[] replaceElements(int[] arr) {
        // int i = 0;
        // while (i<arr.length) {
        //     int current_max = 0;
        //     int j = i+1;
        //     while (j < arr.length){
        //         if (current_max <= arr[j]){
        //             current_max = arr[j];
        //         }
        //         j++;
        //     }
        //     arr[i] = current_max;
        //     i++;
        // }
        // arr[i-1] = -1;
        // return arr;

        int maxVal = -1;
        for (int i = arr.length - 1; i >= 0; i--){
            int current = arr[i];
            arr[i] = maxVal;
            maxVal = Math.max(maxVal, current);
        }
        return arr;
    }
}