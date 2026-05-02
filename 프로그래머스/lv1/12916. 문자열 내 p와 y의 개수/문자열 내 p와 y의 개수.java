class Solution {
	boolean solution(String s) {
		int len = s.length();

		if (len == 0)
			return true;
		
		s = s.toLowerCase();
		int[] arr = new int[2];
		for (int i = 0; i < len; i++) {
			char c = s.charAt(i);
			if (c == 'y')
				arr[0]++;
			else if (c == 'p')
				arr[1]++;
		}

		return arr[0] == arr[1] ? true : false;
	}
}