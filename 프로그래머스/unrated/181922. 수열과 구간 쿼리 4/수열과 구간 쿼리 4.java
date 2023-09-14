class Solution {
    public int[] solution(int[] arr, int[][] queries) {
		int s, e, k;
		for (int[] query : queries) {
			s = query[0];
			e = query[1];
			k = query[2];
			for (int j = s; j <= e; j++)
				if (j % k == 0)
					arr[j]++;
		}

		return arr;
    }
}