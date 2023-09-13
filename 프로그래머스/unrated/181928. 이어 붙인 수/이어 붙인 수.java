class Solution {
    public int solution(int[] num_list) {
		int even = 0, odd = 0;
		for (int num : num_list) {
			if (num % 2 == 0) {
				even *= 10;
				even += num;
				continue;
			}
			odd *= 10;
			odd += num;
		}

		return even + odd;
    }
}