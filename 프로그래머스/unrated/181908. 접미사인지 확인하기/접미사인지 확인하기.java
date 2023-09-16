class Solution {
	public int solution(String str, String isSuffix) {
		int strLen = str.length(), sufLen = isSuffix.length();
		if (sufLen <= strLen && isSuffix.equals(str.substring(strLen - sufLen)))
			return 1;
		return 0;
	}
}