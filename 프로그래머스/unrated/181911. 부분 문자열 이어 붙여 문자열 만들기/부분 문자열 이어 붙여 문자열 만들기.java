class Solution {
	public String solution(String[] strings, int[][] parts) {
		StringBuilder answer = new StringBuilder();
		int length = strings.length;
		for (int i = 0; i < length; i++) {
			answer.append(strings[i].substring(parts[i][0], parts[i][1] + 1));
		}
		return answer.toString();
	}
}