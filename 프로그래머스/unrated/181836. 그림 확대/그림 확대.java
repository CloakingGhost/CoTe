class Solution {
	public String[] solution(String[] picture, int k) {
		int w = picture.length, h = picture[0].length();
		String[] answer = new String[picture.length * k];

		for (int j = 0; j < w; j++) {
			StringBuilder sb = new StringBuilder();
			for (int l = 0; l < h; l++) {
				for (int m = 0; m < k; m++) {
					sb.append(picture[j].charAt(l));
				}
			}
			for (int l = 0; l < k; l++) {
				answer[j * k + l] = sb.toString();
			}
		}
		return answer;
	}
}