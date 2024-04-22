class Solution {
    public String solution(String my_string, int n) {
        String[] arr = my_string.split("");
        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            sb.append(s.repeat(n));
        }
        return sb.toString();
    }
}