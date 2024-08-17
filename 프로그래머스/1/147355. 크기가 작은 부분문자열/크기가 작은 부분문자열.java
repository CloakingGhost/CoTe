class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int tLeng = t.length();
        int pLeng = p.length();
        long intP = Long.parseLong(p);
        for(int i = 0; i < tLeng; i++){
            if(i + pLeng <= tLeng){
                long num = Long.parseLong(t.substring(i, i + pLeng));
                // System.out.println(num);
                if(num <= intP){
                    answer++;
                }
            }
        }
        return answer;
    }
}