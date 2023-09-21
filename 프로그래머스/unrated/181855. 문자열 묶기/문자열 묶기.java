class Solution {
	public int solution(String[] strArr) {
		int[] lengthOfWord = new int[30];
		for (int i = 0; i < strArr.length; i++) {
			lengthOfWord[strArr[i].length() - 1]++;
		}
		int max = 1;
		for(int len : lengthOfWord) {
			if(len > max) {
				max = len;
			}
		}
		return max;
	}
}