import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {
    public int[] solution(int[] emergency) {
        HashMap<Integer, Integer> map = new HashMap<>(){{
            for (int i = 0; i < emergency.length; i++) {
                put(emergency[i], i);
            }
        }};

        int[] idx = map.entrySet().stream().sorted((o1, o2) -> o2.getKey() - o1.getKey()).mapToInt(Map.Entry::getValue).toArray();
        int[] answer = new int[emergency.length];
        for(int i = 0; i < idx.length; i++){
            answer[idx[i]] = i + 1;
        }
        return answer;
    }
}