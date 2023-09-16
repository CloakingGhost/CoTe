import java.util.ArrayList;

class Solution {
	public ArrayList<Integer> solution(String[] strs, int k, int s, int l) {
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (String str : strs) {
			int subString = Integer.parseInt(str.substring(s, s + l));
			if (subString > k) {
				arr.add(subString);
			}
		}
		return arr;
	}

}