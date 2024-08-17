class Solution {
    public String solution(String my_string) {
        char[] chars = my_string.toCharArray();
        for(int i = 0; i < chars.length; i++){
            chars[i] = Character.toLowerCase(chars[i]);
        }
        java.util.Arrays.sort(chars);
        StringBuilder answer = new StringBuilder();
        for(char c : chars){
            answer.append(c);
        }
        return answer.toString();
    }
}