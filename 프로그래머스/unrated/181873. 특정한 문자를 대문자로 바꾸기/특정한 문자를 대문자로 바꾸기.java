class Solution {
	public String solution(String str, String alp) {
		return str.replaceAll(alp, Character.isUpperCase(alp.charAt(0)) ? alp.toLowerCase() : alp.toUpperCase());
	}
}