class Solution {
    public int solution(int[] nums) {
        boolean flag = nums.length < 11;
        int answer = flag ? 1 : 0;
        for(int n : nums){
            if(flag)
                answer *= n;
            else{
                answer += n;
            }
        }
        
        return answer;
    }
}