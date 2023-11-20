class Solution {
    public int solution(int[] sides) {
    	int max = sides[0];
    	int sum = sides[0];
    	for(int i = 1; i < sides.length; i++) {
    		sum += sides[i];
    		if(sides[i] > max) max = sides[i];
    	}
    	sum -= max;
        return max < sum ? 1 : 2;
    }
}