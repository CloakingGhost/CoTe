class Solution {
	public int solution(int price) {
		return price >= 500_000 ? price * 8 / 10
				: price >= 300_000 ? price * 9 / 10 : price >= 100_000 ? price * 95 / 100 : price;
	}
}