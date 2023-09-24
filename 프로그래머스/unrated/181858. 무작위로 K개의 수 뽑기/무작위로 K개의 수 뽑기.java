class Solution {
	public int[] solution(int[] arr, int k) {
		boolean[] chk = new boolean[100_000];
		int[] answer = new int[k];
		int j = 0;
		for (int el : arr) {
			if (j < k && !chk[el]) {
				chk[el] = true;
				answer[j++] = el;
			}
		}
		for (; j < k; j++) answer[j] = -1;

		return answer;
	}
}