class Solution {
	public int[] solution(String[] park, String[] routes) {
		int[] answer = { 0, 0 };
		int xLen = park[0].length();
		int yLen = park.length;
		out: for (int i = 0; i < yLen; i++) {
			for (int j = 0; j < xLen; j++) {
				if (park[i].charAt(j) == 'S') {
					answer[0] = i;
					answer[1] = j;
					break out;
				}
			}
		}
		for (int i = 0; i < routes.length; i++) {
			String[] route = routes[i].split(" ");
			String op = route[0];
			int y = answer[0];
			int x = answer[1];
			int n = Integer.parseInt(route[1]);

			switch (op) {
			case "N":
				if (y - n >= 0) {
					for (int j = 1; j <= n; j++) {
						if (park[y - j].charAt(x) == 'X') {
							answer[0] = y;
							break;
						} else {
							answer[0]--;
						}
					}
				}
				break;
			case "S":
				if (y + n < yLen) {
					for (int j = 1; j <= n; j++) {
						if (park[y + j].charAt(x) == 'X') {
							answer[0] = y;
							break;
						} else {
							answer[0]++;
						}
					}
				}
				break;
			case "W":
				if (x - n >= 0) {
					for (int j = 1; j <= n; j++) {
						if (park[y].charAt(x - j) == 'X') {
							answer[1] = x;
							break;
						} else {
							answer[1]--;
						}
					}
				}
				break;
			case "E":
				if (x + n < xLen) {
					for (int j = 1; j <= n; j++) {
						if (park[y].charAt(x + j) == 'X') {
							answer[1] = x;
							break;
						} else {
							answer[1]++;
						}
					}
				}
				break;
			}
		}
		return answer;
    }
}