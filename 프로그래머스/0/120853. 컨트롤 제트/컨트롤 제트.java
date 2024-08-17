class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] strs = s.split(" ");
        for(int i = strs.length - 1; i >= 0; i--){
            if(strs[i].equals("Z")){
                i--;
            }else {
                answer += Integer.parseInt(strs[i]);
            }
        }
        return answer;
    }
}