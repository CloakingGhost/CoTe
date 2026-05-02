class Solution {
    public int solution(int hp) {
        int[] powers = {5, 3, 1};
        int answer = 0;
        for (int power : powers) {
            answer += hp / power;
            hp %= power;
        }
        return answer;
    }
}