class Solution {
    public int solution(int n) {
        
        int answer = 0;
        int multiply = 1;
        if(n == 1) return 1;
        while (multiply < n){
            multiply *= ++answer;
            if(multiply * (answer + 1) > n) break;
        }
        return answer;
    }
}