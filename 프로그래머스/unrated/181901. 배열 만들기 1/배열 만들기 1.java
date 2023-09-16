import java.util.ArrayList;
class Solution {
public int[] solution(int n, int k) {
        int cnt = n / k;
        int[] answer = new int[cnt];

        for (int i = 1; i <= cnt; i++) {
            answer[i - 1] = k * i;
        }

        return answer;
    }
}