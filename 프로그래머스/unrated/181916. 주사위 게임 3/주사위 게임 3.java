import java.util.Arrays;
import java.util.HashSet;
class Solution {
	public int solution(int a, int b, int c, int d) {
		int[] arr = { a, b, c, d };
		Arrays.sort(arr);
		HashSet<Integer> set = new HashSet<>() {
			{
				add(a);
				add(b);
				add(c);
				add(d);
			}
		};
		switch (set.size()) {
		case 1:
			return 1111 * a;
		case 2:
			int n1, n2;
			for (int i = 0; i < 3; i++) {
				n1 = arr[i]; n2 = arr[i + 1];
                
				if (n1 != n2) {
					if (i == 1)
						return (n1 + n2) * Math.abs(n1 - n2);
					else if (i == 0)
						return (int) Math.pow(10 * n2 + n1, 2);
					return (int) Math.pow(10 * n1 + n2, 2);
				}
			}
		case 3:
			for (int i = 0; i < 3; i++) {
				if (arr[i] == arr[i + 1]) {
					if (i == 0)
						return arr[2] * arr[3];
					else if (i == 1)
						return arr[0] * arr[3];
					return arr[0] * arr[1];
				}
			}
		case 4:
			return arr[0];
		default:
			return 0;
		}
	}
}