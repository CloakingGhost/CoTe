class Solution {
    public int[] solution(int[] nums) {
		java.util.Arrays.sort(nums);

		int[] answer = new int[nums.length - 5];
		int len = answer.length;
		for (int i = 0; i < len; i++) {
			answer[i] = nums[i + 5];
		}
		return answer;
    }
}