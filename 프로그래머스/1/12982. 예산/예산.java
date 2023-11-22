class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        java.util.Arrays.sort(d);
        for(int i = 0; i < d.length; i++) {
        	if(budget < d[i]) break;
        	answer++;
        	budget -= d[i];
        }
        return answer;
    }
}