class Solution {
    public int solution(int a, int b, int c) {
		if (a == b && b == c) {
			return 27 * a * a * a * a * a * a;
		} else if (a == b || a == c || b == c) {
			return (a + b + c) * ((a * a) + (b * b) + (c * c));
		} else {
			return a + b + c;
		}
    }
}