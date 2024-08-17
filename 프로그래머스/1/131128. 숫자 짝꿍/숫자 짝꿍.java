class Solution {
    public String solution(String X, String Y) {
        int[] x = new int[10];
        int[] y = new int[10];
        
        for(int i = 0; i < X.length(); i++){
            int num = (int) X.charAt(i) - '0';
            x[num]++;
        }
        for(int i = 0; i < Y.length(); i++){
            int num = (int) Y.charAt(i) - '0';
            y[num]++;
        }
        
        StringBuilder sb = new StringBuilder();
        for(int i = x.length - 1; i >= 0; i--){
            if(x[i] != 0 && y[i] != 0){
                for(int j = 0; j < Math.min(x[i], y[i]); j++) {
                    sb.append(i);
                }
            }
        }
        if(sb.length() == 0){
            return "-1";
        } else if(sb.charAt(0) == '0'){
            return "0";
        }
        return sb.toString();
        
    }
}