class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        for (char c : my_string.toCharArray()) {
            if (c > 96) {
                sb.append((char)(c - 32));
            } else {
                sb.append((char)(c + 32));
            }
        }
        return sb.toString();
    }
}