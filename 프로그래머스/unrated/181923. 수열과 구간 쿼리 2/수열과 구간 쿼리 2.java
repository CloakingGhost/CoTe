class Solution {
    public int[] solution(int[] arr, int[][] queries) {
		int[] answer = new int[queries.length];
		int length = queries.length;
		int s, e, k;
		for (int i = 0; i < length; i++) {
			int[] query = queries[i];
			s = query[0];
			e = query[1];
			k = query[2];
			int minValue = Integer.MAX_VALUE; // Key Point
			for (int j = s; j <= e; j++) {
				if (arr[j] > k && arr[j] < minValue) {
					minValue = arr[j];
				}
			}
			if (minValue == Integer.MAX_VALUE)
				minValue = -1;
			answer[i] = minValue;

		}
		return answer;
    }
}