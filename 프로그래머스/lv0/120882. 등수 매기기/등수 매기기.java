import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        for(int i = 0; i < score.length; i++){
            for(int j = 0; j < score.length; j++){
                if(answer[i] == 0) answer[i] = 1;
                if(score[i][0] + score[i][1] < score[j][0] + score[j][1]){
                    answer[i] += 1;
                }
            }
        }
        
        return answer;
    }
}