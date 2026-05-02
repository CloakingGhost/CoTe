class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int start = (total / num) - ((num - 1) / 2); // 중앙값(평균값) - 좌우 이격

        for (int i = 0; i < num; i++) {
            answer[i] = start;
            start++;
        }

        return answer;
    }
}