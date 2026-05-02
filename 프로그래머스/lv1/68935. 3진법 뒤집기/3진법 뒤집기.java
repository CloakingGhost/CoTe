class Solution {
	public int solution(int n) {
		StringBuilder sb = new StringBuilder();
		while (n > 0) {
			sb.append(n % 3);
			n /= 3;
		}
		String str = sb.toString();
		return Integer.parseInt(str, 3);
	}
}