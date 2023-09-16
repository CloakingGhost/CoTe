class Solution {
	public int[] solution(int[] arr) {
		int len = 0;
		for (int e : arr)
			len += e;
		int[] answer = new int[len];

		int idx = 0;
		for (int i = 0; i < arr.length; i++) {
			int num = arr[i];
			for (int j = 0; j < num; idx++, j++) {
				answer[idx] = num;
			}

		}

		return answer;
	}
}