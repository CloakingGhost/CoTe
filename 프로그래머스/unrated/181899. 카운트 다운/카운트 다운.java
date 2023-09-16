class Solution {
    public int[] solution(int s, int e) {
		int len = s - e + 1;
		int[] answer = new int[len];
		for (int i = 0; i < len; i++) {
			answer[i] = s--;
		}
		return answer;
    }
}