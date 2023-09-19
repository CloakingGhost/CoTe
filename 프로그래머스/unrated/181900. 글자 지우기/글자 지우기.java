class Solution {
	public String solution(String my_string, int[] indices) {
		String[] arr = my_string.split("");
		for (int i : indices) {
			arr[i] = "";
		}
		StringBuilder sb = new StringBuilder();
		for (String s : arr) sb.append(s);
		return sb.toString();
	}
}