import java.util.*;
class Solution {
    public int solution(int[][] lines) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] line : lines) {
            for (int i = line[0]; i < line[1]; i++) { 
                map.put(i, map.get(i));
            }
        }

       int answer = 0;
       for (int v : map.values()) {
           if (v > 1) {
               answer++;
           }
       }
       return answer;

    }
}