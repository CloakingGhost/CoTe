class Solution {
	public int solution(int a, int d, boolean[] included) {
		int answer = 0;
		int length = included.length;
		for (int i = 0; i < length; i++) {
			if (included[i]) {
				answer += getArithmeticProgression(a, d, i);
			}
		}
		return answer;
	}

	// l = a + (n - 1) * d
	private int getArithmeticProgression(int a, int d, int i) {
		return a + i * d;
	}
}