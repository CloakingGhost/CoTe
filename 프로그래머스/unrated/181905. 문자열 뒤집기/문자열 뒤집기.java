class Solution {
	public String solution(String my_string, int s, int e) {
		String subStr = my_string.substring(s, e + 1);
		StringBuilder sb = new StringBuilder(subStr).reverse();
		return my_string.replace(subStr, sb.toString());
	}
}