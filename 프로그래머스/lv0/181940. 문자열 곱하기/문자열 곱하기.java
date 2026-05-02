class Solution {
    public String solution(String my_string, int k) {
		StringBuffer sb = new StringBuffer(my_string);
		int i = 1;
		while(i++<k) {
			sb.append(my_string);
		}
		return sb.toString();
    }
}