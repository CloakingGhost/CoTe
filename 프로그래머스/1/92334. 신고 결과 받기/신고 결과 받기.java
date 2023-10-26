import java.util.HashMap;
import java.util.HashSet;

class Solution {
	public int[] solution(String[] id_list, String[] report, int k) {
		int[] answer = new int[id_list.length];
		HashMap<String, Integer> idMap = new HashMap<>() {
			{
				int i = 0;
				for (String key : id_list)
					put(key, i++);
			}
		};
		HashMap<String, HashSet<String>> map1 = new HashMap<>() {
			{
				for (String key : id_list)
					put(key, new HashSet<>());
			}
		};
		for (String str : report) {
			String[] origin = str.split(" ");
			map1.get(origin[1]).add(origin[0]);
		}
		for (HashSet<String> arr : map1.values())
			for (String s : arr)
				if (arr.size() >= k) {
					answer[idMap.get(s)]++;
				}
		return answer;
	}
}