class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        for(int i = 0; i < t.length(); i++){
            if(i + p.length() <= t.length()){
                String str = t.substring(i, i + p.length());
                if(str.compareTo(p) < 1){
                    answer++;
                }
            }
        }
        return answer;
    }
}