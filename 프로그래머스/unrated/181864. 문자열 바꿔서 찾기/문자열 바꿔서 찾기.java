class Solution {
	public int solution(String myString, String pat) {
		StringBuilder sb = new StringBuilder(myString);
		int len = sb.length();
		for (int i = 0; i < len; i++) {
			if (sb.charAt(i) == 'A') {
				sb.replace(i, i + 1, "B");
			} else {
				sb.replace(i, i + 1, "A");
			}
		}
		return sb.toString().contains(pat) ? 1 : 0;
	}
}