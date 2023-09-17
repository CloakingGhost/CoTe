class Solution {
    public String solution(String myString) {
        StringBuilder sb = new StringBuilder();
        int len = myString.length();
        char letter;
        for (int i = 0; i < len; i++){
            letter = myString.charAt(i);
            if(letter < 'l'){
                sb.append("l");
            } else{
                sb.append(letter);
            }
            
        }
        return sb.toString();
    }
}