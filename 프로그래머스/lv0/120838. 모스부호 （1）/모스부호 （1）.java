import java.util.*;
class Solution {
    public String solution(String letter) {
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        Map<String, Character> map = new HashMap<>();
        for(int i = 0; i < morse.length; i++){
            map.put(morse[i], (char)(97 + i));
        }
        String[] words = letter.split(" ");
        StringBuilder answer = new StringBuilder();
        for(String word : words){
            answer.append(map.get(word));
        }
        return answer.toString();
    }
}