class Solution {
    public int solution(int[] arr1, int[] arr2) {
		if (arr1.length == arr2.length) {
			int sum = 0;
			for (int a1 : arr1) sum += a1;
			for (int a1 : arr2) sum -= a1;
			return sum == 0 ? 0 : sum > 0 ? 1 : -1;
		} else {
			return arr1.length > arr2.length ? 1 : -1;
		}
    }
}