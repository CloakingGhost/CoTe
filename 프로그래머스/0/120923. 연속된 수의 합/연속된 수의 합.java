class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        for (int i = total; i > Integer.MIN_VALUE; i--) {
            int sum = 0;
            for (int j = 0; j < num; j++) {
                answer[j] = i + j;
                sum += i + j;
            }
            if (sum == total) break;
        }
        return answer;
    }
}