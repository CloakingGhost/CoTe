class Solution {
	public String[] solution(String myStr) {
		String[] arr = myStr.split("[a+b+c+]");
        if(arr.length == 0) return new String[] {"EMPTY"};
		StringBuilder sb = new StringBuilder();
		for(String ele : arr) if(!ele.isEmpty()) {sb.append(ele);sb.append(" ");}
		return sb.toString().split(" ");
	}
}