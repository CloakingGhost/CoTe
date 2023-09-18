class Solution {
	public int[] solution(int[] arr, int[] delete_list) {
		int arrLen = arr.length, delLen = delete_list.length;
		int cnt = arrLen;
		for (int i = 0; i < arrLen; i++) {
			for (int j = 0; j < delLen; j++) {
				if (arr[i] == delete_list[j]) {
					arr[i] = -1;
					cnt--;
					break;
				}
			}
		}
		int[] answer = new int[cnt--];

		for (int i = arrLen - 1; i >= 0; i--) {
			int num = arr[i];
			if (num != -1) answer[cnt--] = num;
			if (cnt == -1) break;
		}
		return answer;
	}
}