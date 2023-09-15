class Solution {
	public String solution(String str, int[][] queries) {
		StringBuilder sb = new StringBuilder(str);
		for (int[] query : queries) {
			int s = query[0];
			int e = query[1];
			StringBuilder subSb = new StringBuilder(sb.substring(s, e + 1));
			sb.replace(s, e + 1, subSb.reverse().toString());
		}
		return sb.toString();
	}
}