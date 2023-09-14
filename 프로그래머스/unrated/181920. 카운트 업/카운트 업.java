class Solution {
    public int[] solution(int s, int e) {
        int length = e - s + 1;
        int[] answer = new int[length];
        for(int i = 0; i < length; i++){
            answer[i] = s++;
        }
        return answer;
    }
}