class Solution {
    public int solution(int[] num_list) {
		StringBuilder evenSb = new StringBuilder();
		StringBuilder oddSb = new StringBuilder();
		for (int num : num_list) {
			if (num % 2 == 0) {
				evenSb.append(num);
				continue;
			}
			oddSb.append(num);
		}

		return Integer.parseInt(evenSb.toString()) + Integer.parseInt(oddSb.toString());
    }
}