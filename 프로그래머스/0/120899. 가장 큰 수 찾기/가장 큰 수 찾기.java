class Solution {
    public int[] solution(int[] array) {
        int maxNum = array[0];
        int idx = 1;
        for(int i = 1; i < array.length; i++) {
            if (array[i] > maxNum) {
                maxNum = array[i];
                idx = i;
            }
        }
        int[] answer = {maxNum, idx};
        return answer;
    }
}