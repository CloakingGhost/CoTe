import java.util.Arrays;
class Solution {
	public String[] solution(String str) {
		int length = str.length();
		String[] answer = new String[length];
		for (int i = 0; i < length; i++) {
			answer[i] = str.substring(i);
		}
		Arrays.sort(answer);
		return answer;
	}
}