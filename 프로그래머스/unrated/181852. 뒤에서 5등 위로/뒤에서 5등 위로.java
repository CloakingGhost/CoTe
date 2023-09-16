class Solution {
    public int[] solution(int[] nums) {
		java.util.Arrays.sort(nums);
		int[] answer = new int[nums.length - 5];
		System.arraycopy(nums, 5, answer, 0, nums.length - 5);
		return answer;
    }
}