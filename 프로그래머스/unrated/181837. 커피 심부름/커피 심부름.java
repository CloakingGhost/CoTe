class Solution {
	public int solution(String[] orders) {
		int answer = 0;
		for (String order : orders) {
			if (order.contains("cafelatte")) {
				answer += 5000;
				continue;
			}
			answer += 4500;
		}
		return answer;
	}
}