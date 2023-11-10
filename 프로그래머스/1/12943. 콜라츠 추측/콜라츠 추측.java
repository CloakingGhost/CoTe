class Solution {
	public int solution(int num) {
		int answer = -1;
		int cnt = 0;
		while (cnt < 501) {
            if (num == 1) {
				return cnt;
			}
			switch (num % 2) {
			case 0:
				num /= 2;
				break;
			case 1:
				num *= 3;
				num++;
				break;
			}
            cnt++;
		}
		return answer;
	}
}