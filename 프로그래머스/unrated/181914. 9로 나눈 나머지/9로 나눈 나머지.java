class Solution {
	public int solution(String number) {
		int length = number.length();
		int i = 0, sum = 0;
		while (i < length)
			sum += Character.getNumericValue(number.charAt(i++));

		return sum % 9;
	}
}