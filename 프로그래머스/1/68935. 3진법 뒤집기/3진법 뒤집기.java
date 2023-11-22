class Solution {
	public int solution(int n) {
		StringBuilder sb = new StringBuilder();
		while (n > 0) {
			sb.append(n % 3);
			n /= 3;
		}
		sb.reverse();
		int size = sb.length();
		int answer = 0;
		for (int i = 0; i < size; i++) {
            answer += (sb.charAt(i) - '0') * Math.pow(3, i);
		}
		return answer;
	}
}