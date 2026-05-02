class Solution {
	public String solution(int n) {
		StringBuffer sf = new StringBuffer();
		for (int i = 0; i < n; ++i) 
			sf.append(i % 2 == 0 ? "수" : "박");
		return sf.toString();
	}
}