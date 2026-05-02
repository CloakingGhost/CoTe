class Solution {
    public String solution(String cipher, int code) {
        StringBuilder answer = new StringBuilder();
        int size = cipher.length();
        for(int i = code - 1; i < size; i += code)
            answer.append(cipher.charAt(i));
        return answer.toString();
    }
}