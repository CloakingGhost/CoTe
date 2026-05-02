class Solution {
    public int solution(String before, String after) {
        char[] b = before.toCharArray();
        char[] a = after.toCharArray();
        java.util.Arrays.sort(b);
        java.util.Arrays.sort(a);
        for(int i = 0; i < b.length; i++){
            if(b[i] != a[i]){
                return 0;
            }
        }
        return 1;
    }
}