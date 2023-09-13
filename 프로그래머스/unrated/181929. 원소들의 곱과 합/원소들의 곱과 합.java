class Solution {
    public int solution(int[] num_list) {
		int mulit = 1, pow = 0;

		for (int num : num_list) {
			mulit *= num;
			pow += num;
		}

		return mulit < pow * pow ? 1 : 0;
    }
}