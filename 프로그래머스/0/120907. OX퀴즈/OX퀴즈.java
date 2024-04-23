class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for (int i = 0; i < quiz.length; i++) {
            String[] quizArr = quiz[i].split(" ");
            int n1 = Integer.parseInt(quizArr[0]);
            int n2 = Integer.parseInt(quizArr[2]);
            String op = quizArr[1];
            switch(op) {
                case "+":
                    if(n1 + n2 == Integer.parseInt(quizArr[4])) {
                        answer[i] = "O";
                    } else {
                        answer[i] = "X";
                    }
                    break;
                case "-":
                    if(n1 - n2 == Integer.parseInt(quizArr[4])) {
                        answer[i] = "O";
                    } else {
                        answer[i] = "X";
                    }
                    break;

            }
        }
        return answer;
    }
}