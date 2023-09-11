class Solution {
	private byte mode = 0;

	public String solution(String code) {
		StringBuilder ret = new StringBuilder();
		int length = code.length();
		char letter;
		boolean isOne;
		for (int i = 0; i < length; i++) {
			letter = code.charAt(i);
			isOne = letter == '1';
			if (isOne) {
				changeMode();
				continue;
			}
			if (isAppending(i)) {
				ret.append(letter);
			}
		}
		return ret.length() == 0 ? "EMPTY" : ret.toString();
	}

	private boolean isAppending(int i) {
		return i % 2 == mode;
	}

	private void changeMode() {
		this.mode = (byte) (mode == 0 ? 1 : 0);
	}

}