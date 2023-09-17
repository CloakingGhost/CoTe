class Solution {
	public String solution(String n_str) {
		int len = n_str.length();
		for (int i = 0; i < len; i++)
			if (n_str.charAt(i) != '0') {
				n_str = n_str.substring(i, len);
				break;
			}
		return n_str;
	}
}