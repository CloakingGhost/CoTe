import java.util.HashMap;
class Solution {
//	public int solution(int[] array) {
//		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
//		for (int key : array)
//			map.put(key, map.getOrDefault(key, 0) + 1);
//
//		int max = -1;
//		int answer = -1;
//		for (int key : map.keySet()) {
//			if (map.get(key) > max) {
//				max = map.get(key);
//				answer = key;
//			}
//		}
//		for (int key : map.keySet()) {
//			if (key != answer && map.get(key) == max)
//				return -1;
//		}
//		return answer;
//	}
    public int solution(int[] array) {
        int maxCount = 0;
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int number : array){
            int count = map.getOrDefault(number, 0) + 1;
            if(count > maxCount){
                maxCount = count;
                answer = number;
            }
            else  if(count == maxCount){
                answer = -1;
            }
            map.put(number, count);
        }
        return answer;
    }
}