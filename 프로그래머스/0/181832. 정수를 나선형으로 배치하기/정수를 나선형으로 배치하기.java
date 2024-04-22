class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int cnt = 1, x = -1, y = 0;
        int loof = n;
        int direction = 1;
        while (cnt <= n * n) {
            for (int i = 0; i < loof; i++) {
                x += direction;
                answer[y][x] = cnt++;
            }
            loof--;
            for (int i = 0; i < loof; i++) {
                y += direction;
                answer[y][x] = cnt++;
            }
            direction *= -1;
        }
        return answer;
    }
}