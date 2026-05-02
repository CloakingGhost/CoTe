import java.util.HashMap;
import java.util.Map;
class Solution {
    public int[] solution(int n, String[] words) {
		int[] answer = { 0, 0 };
		int i = 1;
		Map<String, Integer> map = new HashMap<>();
		map.put(words[0], 1);
		while (i < words.length) {
			if (!check(words[i - 1], words[i])) { // 이전 단어와 현재 단어를 비교
				answer[0] = i % n + 1;
				answer[1] = i / n + 1;
				return answer;
			}
			if (map.containsKey(words[i])) { // 단어 중복 시
				answer[0] = i % n + 1; // 자신의 번호
				answer[1] = i / n + 1; // 자신의 몇 번째 차례인지
				return answer;
			}

			map.put(words[i], 1);
			i++;
		}
		return answer;
	}

	private boolean check(String prev, String curr) {
		char p = prev.charAt(prev.length() - 1);
		char c = curr.charAt(0);
		return p == c;
	}
}