class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
		int len1 = my_string.length();
		int len2 = overwrite_string.length();
		if (!((len2 > 0 && len2 <= len1 && len1 <= 1000) && (s >= 0 && s <= len1 - len2))) {
			return "";
		}

		return new StringBuffer(my_string).replace(s, s+len2, overwrite_string).toString();
    }
}