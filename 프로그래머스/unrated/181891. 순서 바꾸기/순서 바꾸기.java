import java.util.ArrayList;
import java.util.List;
class Solution {
	public Integer[] solution(int[] num_list, int n) {
		int len = num_list.length;
		ArrayList<Integer> arr = new ArrayList<>() {
			{
				for (int i = 0; i < len; i++) {
					if (i < len - n)
						add(num_list[i + n]);
					else
						add(num_list[i - (len - n)]);
				}
			}
		};
		return arr.toArray(new Integer[len]);
	}
}