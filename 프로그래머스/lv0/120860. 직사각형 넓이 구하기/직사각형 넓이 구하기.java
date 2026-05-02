class Solution {
    public int solution(int[][] dots) {
        int maxX = Math.max(Math.max(dots[0][0], dots[1][0]), dots[2][0]); 
        int minX = Math.min(Math.min(dots[0][0], dots[1][0]), dots[2][0]); 
        int maxY = Math.max(Math.max(dots[0][1], dots[1][1]), dots[2][1]);
        int minY = Math.min(Math.min(dots[0][1], dots[1][1]), dots[2][1]);
        
        return Math.abs((maxX - minX) * (maxY - minY));
    }
}