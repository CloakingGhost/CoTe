import java.util.Stack;

class Solution {
    public int[] solution(int[] arr) {
		Stack<Integer> stk = new Stack<>();
		int length = arr.length;
		int i = 0;
		while (i < length) {
			if (stk.isEmpty()) {
				stk.push(arr[i++]);
			} else if (stk.peek() < arr[i]) {
				stk.push(arr[i++]);
			} else {
				stk.pop();
			}
		}
		int size = stk.size();
		int[] answer = new int[size];
		for (int j = size - 1; j >= 0; j--) {
			answer[j] = stk.pop();
		}
		return answer;
    }
}