class Solution {
    public int[] solution(String s) {
        int len = s.length();
        int[] answer = new int[len];
        for(int i = 0; i < len; i++){
            answer[i]--;
            char c = s.charAt(i);
            for(int j = i - 1; j >= 0; j--){
                if(s.charAt(j) == c){
                    answer[i] = i - j;
                    break;
                }
            }
        }
        
        return answer;
    }
}