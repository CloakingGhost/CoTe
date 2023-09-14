import java.util.ArrayList;
class Solution {
    public int[] solution(int l, int r) {
		l -= (l % 5);
		if (l == 0)
			l = 5;
		r -= (r % 5);

		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = l; i <= r; i += 5) {
			if (i % 5 == 0) {
				try {
					Integer.parseInt(i / 5 + "", 2);
					arr.add(i);
				} catch (Exception e) {
				}
			}
		}
		int[] answer = { -1 };
		int size = arr.size();
		if (size == 0)
			return answer;
		answer = new int[arr.size()];
		for (int i = 0; i < size; i++) {
			answer[i] = arr.get(i);
		}
		return answer;
    }
}