class Solution {
    public String solution(String rsp) {
        StringBuilder answer = new StringBuilder();
        for(char c : rsp.toCharArray()){
            if (c == '0') answer.append('5');
            else if (c == '2') answer.append('0');
            else if (c == '5') answer.append('2');
        }
        return answer.toString();
    }
}