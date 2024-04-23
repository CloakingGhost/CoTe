import java.util.Arrays;
class Solution {
    public int solution(int[][] lines) {
        int[] cnts = new int[201]; 
        for (int[] line : lines) {
            ++cnts[line[0] + 100];
            --cnts[line[1] + 100];
        }
        int answer = cnts[0] > 1 ? 1 : 0;
        for (int i = 1; i < 201; ++i) {
            cnts[i] += cnts[i - 1];
            if (cnts[i] > 1) ++answer;
        }
        return answer;
    }
}