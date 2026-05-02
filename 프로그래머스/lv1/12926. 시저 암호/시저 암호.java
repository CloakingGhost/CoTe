class Solution {
    public String solution(String s, int n) {
        int length = s.length();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < length; i++){
            char c = s.charAt(i);
            if(c == 32) {
                sb.append(c);
                continue;
            }
            else{
                if(c > 96 && c + n > 122) c -= 26;
                else if(c < 97 && c + n > 90) c -= 26;
            }
            c += n;
            sb.append(c);
        }
        return sb.toString();
    }
}