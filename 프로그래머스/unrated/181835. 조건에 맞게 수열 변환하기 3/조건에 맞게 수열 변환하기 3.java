class Solution {
    public int[] solution(int[] arr, int k) {
        boolean isOdd = k % 2 == 1;
        int length = arr.length;
        for (int i = 0; i < length; i++){
            if(isOdd) arr[i] *= k;
            else arr[i] += k;
        }
        return arr;
    }
}