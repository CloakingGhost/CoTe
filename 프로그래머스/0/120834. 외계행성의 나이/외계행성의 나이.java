class Solution {
    public String solution(int age) {
        StringBuilder answer = new StringBuilder();
        for (char c : String.valueOf(age).toCharArray()) {
            answer.append((char) (c + 49));
        }

        return answer.toString();
    }
}