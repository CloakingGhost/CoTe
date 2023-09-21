class Solution {
	public int solution(int[] arr) {
		int cnt = 0, len = arr.length;
		while (true) {
			int i = 0, prev = 0, matching = 0;
			while (i < len) {
				prev = arr[i];
				if (prev >= 50 && prev % 2 == 0) arr[i] /= 2;
				else if (prev < 50 && prev % 2 == 1) arr[i] = arr[i] * 2 + 1;

				if (prev == arr[i]) matching++;
				i++;
			}
			if (matching == len) return cnt;
			cnt++;
		}
	}
}