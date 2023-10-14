import java.util.HashMap;
class Solution {
	public int solution(int[] array) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int key : array)
			map.put(key, map.getOrDefault(key, 0) + 1);

		int max = -1;
		int answer = -1;
		for (int key : map.keySet()) {
			if (map.get(key) > max) {
				max = map.get(key);
				answer = key;
			}
		}
		for (int key : map.keySet()) {
			if (key != answer && map.get(key) == max)
				return -1;
		}
		return answer;
	}
}