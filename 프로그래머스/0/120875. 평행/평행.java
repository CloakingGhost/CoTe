class Solution {
    public int solution(int[][] dots) {
        for (int i = 0; i < 4; i++) {
            float slope1 = slope(dots[i], dots[(i + 1) % 4]);
            float slope2 = slope(dots[(i + 2) % 4], dots[(i + 3) % 4]);

            if (isParallel(slope1, slope2)) return 1;
        }
        return 0;
    }

    public float slope(int[] dot1, int[] dot2) {
        return (float) (dot2[1] - dot1[1]) / (dot2[0] - dot1[0]);
    }

    private boolean isParallel(float slope1, float slope2) {
        return slope1 == slope2;
    }
}