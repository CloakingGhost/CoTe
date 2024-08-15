class Solution {
    public int solution(int balls, int share) {
        int[][] dp = new int[balls + 1][share + 1];

        for (int i = 0; i <= balls; i++) {
            for (int j = 0; j <= Math.min(i, share); j++) {
                if (j == 0 || j == i) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                }
            }
        }
        return dp[balls][share];
    }
}