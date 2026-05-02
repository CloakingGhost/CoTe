import java.util.Arrays;
class Solution {
	public long solution(long n) {
		char[] chars = String.valueOf(n).toCharArray();
		Arrays.sort(chars);
		StringBuilder sb = new StringBuilder(new String(chars));
		String str = sb.reverse().toString();
		long answer = Long.parseLong(str);
		return answer;
	}
}