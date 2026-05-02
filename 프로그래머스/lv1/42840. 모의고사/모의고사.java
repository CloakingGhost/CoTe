class Solution {
    public int[] solution(int[] answers) {
        int[] s1 = {1, 2, 3, 4, 5};
        int[] s2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] s3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int [][] s = {s1, s2, s3};
        int[] counts = new int[s.length];
        for(int i = 0; i < answers.length; i++){
            for(int j = 0; j < counts.length; j++){
                counts[j] += s[j][i % s[j].length] == answers[i] ? 1 : 0;
            }
        }
        int maxC = -1;
        for(int c : counts){
            maxC = Math.max(maxC, c);
        }
        
        boolean[] visited = new boolean[s.length];
        int maxCount = 0;
        for(int i = 0; i < visited.length; i++){
            if(counts[i] == maxC){
                visited[i] = true;
                maxCount++;
            }
        }
        
        
        int[] answer = new int[maxCount];
        int idx = 0;
        for(int i = 0; i < visited.length; i++){
            if(visited[i]){
                answer[idx++] = i + 1;
            }
        }
        return answer;
    }
}