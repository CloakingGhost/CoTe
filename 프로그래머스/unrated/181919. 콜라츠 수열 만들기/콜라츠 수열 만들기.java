import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
		ArrayList<Integer> arr = new ArrayList<Integer>();
		arr.add(n);
		while (n > 1) {
			n = n % 2 == 0 ? n / 2 : 3 * n + 1;
			arr.add(n);
		}
		int size = arr.size();
		int[] answer = new int[size];
		for (int i = 0; i < size; i++) {
			answer[i] = arr.get(i);
		}
		return answer;
    }
}