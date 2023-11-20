class Solution {
	public int solution(String[] babbling) {
		int answer = 0;
		for (int i = 0; i < babbling.length; i++) {
			String str = babbling[i].replaceAll("(aya|ye|woo|ma)?", "");
			if (str.isBlank())
				answer++;
		}
		return answer;
	}
}