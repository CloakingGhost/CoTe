import java.util.Stack;
class Solution {
	public int[] solution(int[] arr) {
		Stack<Integer> stk = new Stack<>();
		
		for (int i = 0; i < arr.length; i++) 
			if (stk.empty()) stk.push(arr[i]);
			else if (stk.peek() == arr[i]) stk.pop();
			else stk.push(arr[i]);
		int size = stk.size();
		if (size == 0) return new int[] { -1 };
		int[] answer = new int[size];
		for (int i = 0; i < size; i++) answer[i] = stk.get(i);
		return answer;
	}
}