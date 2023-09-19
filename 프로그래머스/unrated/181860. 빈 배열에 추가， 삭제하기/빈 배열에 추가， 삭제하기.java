import java.util.ArrayList;

class Solution {
	public int[] solution(int[] arr, boolean[] flag) {
		ArrayList<Integer> arrList = new ArrayList<>();
		for (int i = 0; i < arr.length; i++) {
			int num = arr[i];
			if (flag[i]) {
				for (int j = 0; j < num * 2; j++) {
					arrList.add(num);
				}
			} else {
				for (int j = 0; j < num; j++)
					arrList.remove(arrList.size() - 1);
			}
		}
		int[] answer = new int[arrList.size()];
		int i = 0;
		for (int ele : arrList) {
			answer[i++] = ele;
		}

		return answer;
	}
}