class Solution {
	public String[] solution(String[] strArr) {
		int len = strArr.length;
		int idx = 0;
		int cnt = len;
		for (String str : strArr) {
			if (str.contains("ad")) {
				strArr[idx] = "";
				cnt--;
			}
			idx++;
		}
		String[] answer = new String[cnt--];

		for (int i = len - 1; i >= 0; i--) {

			if (!strArr[i].isBlank()) {
				answer[cnt--] = strArr[i];
			}
		}
		return answer;
	}
}