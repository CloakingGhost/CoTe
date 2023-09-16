import java.util.Arrays;
class Solution {
	public int[] solution(int[] arr, int[] query) {
		int qLen = query.length;
		for (int i = 0; i < qLen; i++) {
			if (i % 2 == 0) {
				arr = Arrays.copyOfRange(arr, 0, query[i] + 1); // 짝수 인덱스 뒤부분 제거 == 앞에서부터 인덱스까지 복사
			} else {
				arr = Arrays.copyOfRange(arr, query[i], arr.length); // 홀수 인덱스 앞부분 제거 == 인덱스부터 배열(혹은 복사된 배열)의 길이만큼 복사
			}
		}
		return arr;
	}
}