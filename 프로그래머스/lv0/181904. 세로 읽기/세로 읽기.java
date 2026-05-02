class Solution {
	public String solution(String my_string, int m, int c) {
		StringBuilder sb = new StringBuilder();
		int len = my_string.length();
		for (int i = c - 1; i < len; i += m) {
			sb.append(my_string.charAt(i));
		}
		return sb.toString();
	}
}