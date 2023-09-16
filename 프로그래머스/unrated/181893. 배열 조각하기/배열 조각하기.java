import java.util.Arrays;
class Solution {
	public int[] solution(int[] arr, int[] query) {
		int qLen = query.length;
		int s = 0, e = arr.length - 1;

		for (int i = 0; i < qLen; i++) {
			if (i % 2 == 0) {
				e -= e - query[i] - s - 1;
			} else {
				s += query[i];
			}
		}
		return Arrays.copyOfRange(arr, s, e);
	}
}