class Solution {
    public int solution(int n) {
        int answer = 0;
		switch (n % 2) {
		case 0:
			int i = 2;
			while (i <= n) {
				answer += i * i;
				i += 2;
			}
			break;
		case 1:
			answer = (n+1)*(n+1)/4;

			break;
		}
		return answer;
    }
}