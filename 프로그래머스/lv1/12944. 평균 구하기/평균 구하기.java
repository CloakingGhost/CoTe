class Solution {
	public double solution(int[] arr) {
		double answer = 0;
		int len = arr.length;
		for (int i = 0; i < len; i++)
			answer += arr[i];
		return answer / len;
	}
}