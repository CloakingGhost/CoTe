import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int divisor) {
		ArrayList<Integer> array = new ArrayList<>();
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] % divisor == 0)
				array.add(arr[i]);
		}
		if (array.isEmpty())
			array.add(-1);
		int size = array.size();
		int[] answer = new int[size];
		for (int i = 0; i < size; i++) {
			answer[i] = array.get(i);
		}
		Arrays.sort(answer);
		return answer;
	}
}