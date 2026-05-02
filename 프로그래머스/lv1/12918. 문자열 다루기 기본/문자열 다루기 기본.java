class Solution {
	public boolean solution(String s) {
        if(s.length() == 4 ||s.length() == 6)
		return s.matches("^[\\d]*$");
        return false;
	}
}