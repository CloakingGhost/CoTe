class Solution {
	public String solution(String s) {
		int begin = s.length() % 2 == 0 ? s.length() / 2 - 1 : s.length() / 2;
		int end = s.length() / 2 + 1;
		String str = s.substring(begin, end);
		return str;
	}
}