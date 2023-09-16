class Solution {
	public int solution(String str, String isSuffix) {
		if (str.endsWith(isSuffix))
			return 1;
		return 0;
	}
}