class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        StringBuilder sb = new StringBuilder()	;
        
        int len = todo_list.length;
        for (int i = 0; i < len; i++){
            if(!finished[i]){
            	sb.append(todo_list[i]);
                sb.append(" ");
            }
        }
        return sb.toString().split("\\s+");
    }
}