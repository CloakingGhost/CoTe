class Solution {
    public String solution(int[] numLog) {
		int length = numLog.length;
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < length; i++) {
			switch (numLog[i] - numLog[i - 1]) {
			case 1:
				sb.append("w");
				break;
			case -10:
				sb.append("a");
				break;
			case -1:
				sb.append("s");
				break;
			default:
				sb.append("d");
			}
		}
		return sb.toString();
    }
}