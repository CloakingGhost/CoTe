class Solution {
    public int[] solution(int[] arr, int n) {
        int len = arr.length;
        int i = len % 2 == 0 ? 1 : 0;
        for (; i < len; i += 2)
            arr[i] += n;

        return arr;
    }
}