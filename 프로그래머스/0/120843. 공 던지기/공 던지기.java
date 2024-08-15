class Solution {
    public int solution(int[] numbers, int k) {
        int answer = numbers[0];
        int turn = 0;
        for(int i = 1; i <= k; i++){
            answer = numbers[turn % numbers.length];
            turn = (turn + 2) % numbers.length;
            
        }
        return answer;
    }
}