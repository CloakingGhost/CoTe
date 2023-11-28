class Solution {
	public int solution(String[][] board, int h, int w) {
		int answer = 0;
		int n = board.length;
		int[] dh = { 0, 1, -1, 0 }; // 세로
		int[] dw = { 1, 0, 0, -1 }; // 가로
		for (int i = 0; i < 4; i++) {
			int h_chk = h + dh[i];
			int w_chk = w + dw[i];
			if (h_chk >= 0 && h_chk < n && w_chk >= 0 && w_chk < n) {
				if (board[h][w].equals(board[h_chk][w_chk]))
					answer++;
			}
		}
		return answer;
	}
}