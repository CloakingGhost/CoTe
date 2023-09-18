import java.util.Arrays;
class Solution {
	public String[] solution(String myString) {
		String[] answer = myString.split("[x+^\\s]");
		Arrays.sort(answer);
		int i = 0;
		for (String str : answer) {
			if (!str.isBlank()) {
				return Arrays.copyOfRange(answer, i, answer.length);
			}
			i++;
		}
		return answer;
	}
}