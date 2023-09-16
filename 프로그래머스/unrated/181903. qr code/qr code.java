class Solution {
	public String solution(int q, int r, String code) {
		int len = code.length();
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < len; i++) {
			if (i % q == r)
				sb.append(code.charAt(i));
		}
		return sb.toString();
	}
}