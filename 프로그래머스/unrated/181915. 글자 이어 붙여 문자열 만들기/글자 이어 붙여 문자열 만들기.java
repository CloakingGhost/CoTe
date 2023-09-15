class Solution {
	public String solution(String string, int[] idxList) {
		int length = idxList.length;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < length; i++) {
			sb.append(string.charAt(idxList[i]));
		}

		return sb.toString();
	}
}