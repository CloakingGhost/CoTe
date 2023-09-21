import java.util.Arrays;
class Solution {
	public int[] solution(int n, int[] slicer, int[] num_list) {
		int a = slicer[0], b = slicer[1] + 1, c = slicer[2];
		int[] answer = {};
		switch (n) {
		case 1:
			return Arrays.copyOf(num_list, b);
		case 2:
			return Arrays.copyOfRange(num_list, a, num_list.length);
		case 3:
			return Arrays.copyOfRange(num_list, a, b);
		case 4:
			int len = (b - 1 - a) / c + 1;
			answer = new int[len];
			for (int i = 0; i < len; i++)
				answer[i] = num_list[a + i * c];
		}
		return answer;
	}
}