import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Comparator;
class Solution {
	public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
		HashMap<String, Integer> map = new HashMap<>();
		map.put("code", 0);
		map.put("date", 1);
		map.put("maximum", 2);
		map.put("remain", 3);
		int extIdx = map.get(ext);
		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = 0; i < data.length; i++) {
			if (data[i][extIdx] < val_ext) {
				arr.add(i);
			}
		}
		int size = arr.size();
		int sortIdx = map.get(sort_by);
		int[][] answer = new int[size][data[0].length];
		for (int i = 0; i < size; i++) {
			answer[i] = Arrays.copyOf(data[arr.get(i)], data[arr.get(i)].length);
		}
		Arrays.sort(answer, new Comparator<int[]>() {
			@Override
			public int compare(int[] s1, int[] s2) {
				return s1[sortIdx] - s2[sortIdx];
			}
		});
		// sort(answer, sortIdx);
		return answer;
	}

	public static void sort(int[][] array, int idx) {
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length - 1; j++) {
				if (array[j][idx] > array[j + 1][idx]) {
					int[] tmp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = tmp;
				}
			}
		}
	}
}