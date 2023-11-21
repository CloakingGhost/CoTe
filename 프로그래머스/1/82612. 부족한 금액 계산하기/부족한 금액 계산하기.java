class Solution {
	public long solution(int price, int money, int count) {
		long tmp = price * (1 + count);
		long payment = count * tmp / 2;
		long answer = payment > money ? payment - money : 0;
		return answer;
	}
}