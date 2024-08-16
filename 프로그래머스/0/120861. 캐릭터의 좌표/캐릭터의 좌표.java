class Solution {
    public int[] solution(String[] keyinput, int[] board) {
    
        int[] answer = {0, 0};

        // 올바른 함수 넣기
        for(String key : keyinput){
            switch(key){
                case "up":
                    if(answer[1] + 1 <= board[1] / 2)
                        func1(answer);
                    break;
                case "down":
                    if(answer[1] - 1 >= -(board[1] / 2))
                        func4(answer);
                    break;
                case "right":
                    if(answer[0] + 1 <= board[0] / 2)
                        func3(answer);
                    break;
                default:
                    if(answer[0] - 1 >= -(board[0] / 2))
                        func2(answer);
            }
        }
        
        return answer;
    }
    
    
    private void func1(int[] arr){
        arr[1]++;
    }
    
    private void func2(int[] arr){
        arr[0]--;
    }
    
    private void func3(int[] arr){
        arr[0]++;
    }
    
    private void func4(int[] arr){
        arr[1]--;
    }
    
}