class Solution {
	public int solution(String myString, String pat) {
		int post = -1;
		int answer = 0;
		for (int i = 0; i < myString.length(); i++) {
			int idx = myString.indexOf(pat, i);

			if (idx != -1 && idx != post) {
				answer++;
				post = idx;
			}
		}
		return answer;
	}
}