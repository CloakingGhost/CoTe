import java.util.ArrayList;
import java.util.HashMap;

public class Solution {
	public int[] solution(String today, String[] terms, String[] privacies) {
		int nowday = converter(today, 0);

		HashMap<String, Integer> map = new HashMap<>();
		for (int i = 0; i < terms.length; i++) {
			String[] str = terms[i].split(" ");
			map.put(str[0], Integer.parseInt(str[1]));
		}
		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = 0; i < privacies.length; i++) {
			String[] str = privacies[i].split(" ");
			String agreeDay = str[0];
			int month = map.get(str[1]);

			if (nowday > converter(agreeDay, month) - 1)
				arr.add(i + 1);
		}
		int size = arr.size();
		int[] answer = new int[size];
		for (int i = 0; i < size; i++) {
			answer[i] = arr.get(i);
		}
		return answer;
	}

	private static int converter(String day, int policy) {
		String[] str = day.split("[.]");
		int sum = Integer.parseInt(str[0]) * 12 * 28 + (Integer.parseInt(str[1]) + policy) * 28
				+ Integer.parseInt(str[2]);
		return sum;
	}
}