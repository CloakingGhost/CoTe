import java.util.HashMap;
import java.util.Map;
class Solution {
    public int[] solution(int[] numlist, int n) {
        HashMap<Integer, Integer> map = new HashMap<>() {{
            for (int j : numlist) {
                put(j, Math.abs(j - n));
            }
        }};

        return map.entrySet().stream()
                .sorted((o1, o2) -> o1.getValue().intValue() ==  o2.getValue().intValue() ? o2.getKey() - o1.getKey() : o1.getValue() - o2.getValue())
                .mapToInt(Map.Entry::getKey)
                .toArray();
        
    }
}