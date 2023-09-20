class Solution {
	public int[] solution(int[] arr) {
		int binary = 1;
		while (binary < arr.length) {
			binary *= 2;
		}
		if (binary == arr.length)
			return arr;
		else {
			int[] answer = new int[binary];
			System.arraycopy(arr, 0, answer, 0, arr.length);
			return answer;
		}

	}
}