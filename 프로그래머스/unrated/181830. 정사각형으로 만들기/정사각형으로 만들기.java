class Solution {
	public int[][] solution(int[][] arr) {
		int row = arr.length;
		int column = arr[0].length;
		if (row == column)
			return arr;

		int[][] answer = new int[column][column];
		if (row > column) answer = new int[row][row];
		
		for (int i = 0; i < row; i++) 
			System.arraycopy(arr[i], 0, answer[i], 0, column);

		return answer;
	}
}