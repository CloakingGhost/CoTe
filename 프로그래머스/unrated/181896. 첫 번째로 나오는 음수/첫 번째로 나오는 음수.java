class Solution {
    public int solution(int[] nums) {
        int length = nums.length;
        for(int i = 0; i < length; i++){
            if(nums[i] < 0) return i;            
        }
        return -1;
    }
}