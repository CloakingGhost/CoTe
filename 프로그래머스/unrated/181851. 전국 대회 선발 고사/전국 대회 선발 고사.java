class Solution {
	public int solution(int[] rank, boolean[] attendance) {
		int answer = 0, cnt = 0;
		for (int i = 0; i < rank.length && cnt < 3; i++) {
			for (int j = 0; j < rank.length; j++) {
				if (attendance[j] && rank[j] == i + 1) {
					answer += j * (int) Math.pow(100, 2 - cnt++);
				}
			}
		}

		return answer;

	}
}