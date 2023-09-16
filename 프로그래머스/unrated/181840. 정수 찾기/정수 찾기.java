class Solution {
    public int solution(int[] nums, int n) {
        return java.util.stream.IntStream.of(nums).anyMatch(num -> num == n) ? 1 : 0;
    }
}