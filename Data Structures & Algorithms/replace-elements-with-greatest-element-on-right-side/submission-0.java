class Solution {
    // public int[] swapElements(int i, int j, int[] arr){
    //     int temp = arr[i];
    //     arr[i] = arr[j];
    //     arr[j] = temp;
    //     return arr;
    // }

    public int[] replaceElements(int[] arr) {
        int i = 0;
        while (i<arr.length) {
            int current_max = 0;
            int j = i+1;
            while (j < arr.length){
                if (current_max <= arr[j]){
                    current_max = arr[j];
                }
                j++;
            }
            arr[i] = current_max;
            i++;
        }
        arr[i-1] = -1;
        return arr;
    }
}