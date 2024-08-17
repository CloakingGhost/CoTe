class Solution {
    public String[] solution(String my_str, int n) {
        int leng = my_str.length() / n + (my_str.length() % n == 0 ? 0 : 1);
        String[] answer = new String[leng];
        int s = 0, e = n;
        for(int i = 0; i < leng; i++){
            if(e > my_str.length()){
                answer[i] = my_str.substring(s, my_str.length());
                break;
            }

            answer[i] = my_str.substring(s, e);
            s += n;
            e += n;
        }
        return answer;
    }
}