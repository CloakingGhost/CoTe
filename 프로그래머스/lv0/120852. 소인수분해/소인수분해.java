class Solution {
    public int[] solution(int n) {
        java.util.ArrayList<Integer> arr = new java.util.ArrayList<>();
        int prime = 2;
        while(n > 1){
            if(isPrime(prime)){
                System.out.println(prime);
                while(n / prime != 0 && n % prime == 0) {
                        n /= prime;
                    if(!arr.contains(prime)) {
                        arr.add(prime);
                     }
                }
            }
            prime++;
        }
        
        int[] answer = new int[arr.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = arr.get(i);
        }
        return answer;
    }
    
    private boolean isPrime(int num){
        for(int i = 2; i <= num / 2; i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}