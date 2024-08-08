class Solution {
    public int[] solution(String[] keyinput, int[] board) {
    
        int[] answer = {0, 0};

        for(String key : keyinput){
            switch(key){
                case "up":
                    if(answer[1] + 1 <= board[1] / 2)
                        answer[1]++;
                    break;
                case "down":
                    if(answer[1] - 1 >= -(board[1] / 2))
                        answer[1]--;
                    break;
                case "right":
                    if(answer[0] + 1 <= board[0] / 2)
                        answer[0]++;
                    break;
                default:
                    if(answer[0] - 1 >= -(board[0] / 2))
                        answer[0]--;
            }
        }
        
        return answer;
    }
    
}