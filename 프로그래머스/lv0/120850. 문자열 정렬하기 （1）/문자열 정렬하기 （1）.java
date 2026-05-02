import java.util.Arrays;
class Solution {
    public int[] solution(String my_string) {
        String[] s = my_string.split("");
        Arrays.sort(s);
        int[] answer = {};
        
        if(s[s.length - 1].compareTo("9") <= 0) {
            answer = new int[s.length];
        } else {
            for(int i = 0; i < s.length; i++){
                if(s[i].compareTo("9") > 0){
                    answer = new int[i];
                    break;
                }
            }
        }
        
        for(int i = 0; i < answer.length; i++){
            answer[i] = Integer.parseInt(s[i]);
        }
        
        
        return answer;
    }
}