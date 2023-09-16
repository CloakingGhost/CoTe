class Solution {
    public int solution(String nums) {
		int length = nums.length();
		int answer = 0;
		for (int i = 0; i < length; i++) {
			answer += nums.charAt(i) - '0';
		}
        
        return answer;
    }
}