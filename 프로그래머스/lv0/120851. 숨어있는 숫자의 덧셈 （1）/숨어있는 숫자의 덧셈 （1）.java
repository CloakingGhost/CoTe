class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(char c : my_string.toCharArray()){
            if (c < 58){
                answer += c - 48;
            }
        }
        return answer;
    }
}