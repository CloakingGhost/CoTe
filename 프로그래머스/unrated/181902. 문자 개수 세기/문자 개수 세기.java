class Solution {
	public int[] solution(String my_string) {
		int[] answer = new int[52];
		for (int i = 0; i < my_string.length(); i++) {
			int idx = my_string.charAt(i) > 96 ? my_string.charAt(i) - 97 + 26 : my_string.charAt(i) - 65;
			answer[idx]++;
		}
		return answer;
	}
}