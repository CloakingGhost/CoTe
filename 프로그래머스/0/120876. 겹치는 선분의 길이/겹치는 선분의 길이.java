import java.util.*;
class Solution {
    public int solution(int[][] lines) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] line : lines) {// 직선 하나 가져온다(좌표값)
            for (int i = line[0]; i < line[1]; i++) { // 좌표 시작값 부터 끝값 직전까지 맵에 넣기
                map.put(i, map.getOrDefault(i, 0) + 1);
            }
        }
//        아래 스트림 대신 가능
//        int answer = 0;
//        for (int v : map.values()) {
//            if (v > 1) {
//                answer++;
//            }
//        }
//        return answer;
        return (int) map.values().stream().filter(v -> v > 1).count(); // 2 이상인 값들을 카운트
    }
}