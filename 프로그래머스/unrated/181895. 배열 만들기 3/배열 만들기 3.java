class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int len = 0;
        
        
        int idx = 0;
        for(int[] inter : intervals){
            len += inter[1] - inter[0] + 1;
        }
        int[] answer = new int[len];
        idx = 0;
        for(int[] inter : intervals){
            for(int i = inter[0]; i <= inter[1]; i++){
                answer[idx++] = arr[i];
            }
        }
        return answer;
    }
}