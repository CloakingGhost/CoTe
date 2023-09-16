class Solution {
    public String[] solution(String[] names) {
        String[] answer = new String[((names.length - 1) / 5) + 1];
        int len = answer.length;
        for(int i = 0, j = 0; i < len; i++, j += 5){
            answer[i] = names[j];
        }
        return answer;
    }
}