class Solution {
    public String solution(String polynomial) {
        String[] arr = polynomial.split(" ");
        int[] answerArr = new int[2];
        for (int i = 0; i < arr.length; i += 2) {
            if (arr[i].contains("x")) {
                String str = arr[i].replace("x", "");
                if (str.isEmpty()) {
                    answerArr[0] += 1;
                    continue;
                }
                answerArr[0] += Integer.parseInt(str);
            } else {
                answerArr[1] += Integer.parseInt(arr[i]);
            }
        }
        String answer = "";
        if (answerArr[0] != 0) {
            answer += answerArr[0] == 1 ? "x" : answerArr[0] + "x";
        }
        if (answerArr[1] != 0) {
            answer += answer.isEmpty() ? answer + answerArr[1] : " + " + answerArr[1];
        }
        return answer;
    }
}