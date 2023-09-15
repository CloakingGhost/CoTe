import java.util.Stack;

class Solution {
    public Stack<Integer> solution(int[] arr) {
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
		return stk;
    }
}