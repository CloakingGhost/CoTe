class Solution {
	public String solution(int n) {
		char[] chars = new char[n];
		for (int i = 0; i < n / 2; i++) {
			chars[2 * i] = '수';
			chars[2 * i + 1] = '박';
		}
		if (n % 2 == 1)
			chars[n - 1] = '수';
		return String.valueOf(chars);
	}
}