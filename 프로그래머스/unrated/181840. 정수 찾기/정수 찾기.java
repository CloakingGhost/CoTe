class Solution {
    public int solution(int[] nums, int n) {
		for (int e : nums)
			if (e == n)
				return 1;
        return 0;
    }
}