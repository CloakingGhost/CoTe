class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] nums = my_string.split(" ");
        answer = Integer.parseInt(nums[0]);
        for(int i = 1; i < nums.length; i += 2){
            if(nums[i].equals("+")){
                answer += Integer.parseInt(nums[i + 1]); 
            } else {
                answer -= Integer.parseInt(nums[i + 1]);
            }
        }
        return answer;
    }
}