class Solution {
	public int solution(int[][] arr) {
		int len1 = arr.length, len2 = arr[0].length;
		for (int i = 0; i < len1; i++)
			for (int j = 0; j < len2; j++)
				if (arr[i][j] != arr[j][i])
					return 0;
		return 1;
	}
}