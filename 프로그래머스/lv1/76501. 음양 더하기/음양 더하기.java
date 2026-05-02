class Solution {
	public int solution(int[] absolutes, boolean[] signs) {
		int answer = 0, num = 0;
		for (int i = 0; i < signs.length; i++) {
			num = absolutes[i];
			if (!signs[i])
				num = -num;
			answer += num;
		}
		return answer;
	}
}