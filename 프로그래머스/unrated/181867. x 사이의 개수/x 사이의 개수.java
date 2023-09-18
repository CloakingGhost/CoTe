class Solution {
	public int[] solution(String myString) {
		String[] strList = myString.split("x", -1);
		int[] answer = new int[strList.length];

		int i = 0;
		for (String str : strList) {
			answer[i++] = str.length();
		}
		return answer;
	}
}