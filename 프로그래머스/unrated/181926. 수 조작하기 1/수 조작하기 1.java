class Solution {
    public int solution(int n, String control) {
		int length = control.length();
		for (int i = 0; i < length; i++) {
			switch (control.charAt(i)) {
			case 'w':
				n++;
				break;
			case 'a':
				n -= 10;
				break;
			case 's':
				n--;
				break;
			default:
				n += 10;
			}
		}
		return n;
    }
}