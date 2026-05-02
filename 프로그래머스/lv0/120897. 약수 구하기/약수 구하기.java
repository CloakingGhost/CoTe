import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();  
        int limit = (int) Math.sqrt(n);
        for(int i = 1; i <= limit; i++){
            if(n % i == 0){
                arr.add(i);
                if(i != n / i) {
                    arr.add(n / i);
                }
            }
        }  
        arr.sort(Integer::compareTo);
        int[] answer = new int [arr.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}