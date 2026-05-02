class Solution {
	public int[] solution(int[] arr) {
		if (arr.length == 1) {
			arr[0] = -1;
			return arr;
		}
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] < min)
				min = arr[i];
		}
		int[] answer = new int[arr.length - 1];
		int idx = 0;
		for (int num : arr) {
			if (num != min)
				answer[idx++] = num;

		}
		return answer;
	}
}