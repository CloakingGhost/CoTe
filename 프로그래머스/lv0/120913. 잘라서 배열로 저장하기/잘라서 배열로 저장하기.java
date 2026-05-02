class Solution {
    public String[] solution(String my_str, int n) {
        // 1. 정답을 위한 문자열 배열을 담을 answer 선언
        // 1-1. 배열의 길이로 정수 타입의 변수 leng을 선언하여 주어진 문자열을 n으로 나눈값과 
        //     주어진 문자열을 n으로 나누었을 때 나머지가 있으면 1을 더한 값을 담는다.
        // 2. 문자열을 자를 구간 설정을 위한
        //    정수 타입의 변수 start, end 선언하여 0, n으로 초기화한다.
        // 3. 반복문을 사용하여 answer의 길이 만큼 반복하여 start와 end를 n 만큼 증가
        // 3-1. 조건문을 통해 end의 값이 주어진 문자열의 길이보다 작으면
        //      정답 배열의 값으로 주어진 문자열을 start부터 end까지 담는다
        // 3-2. 그렇지 않다면 
        //      정답 배열의 값으로 주어진 문자열을 start부터 주어진 문자열 길이만큼 잘라 담는다
        int leng = my_str.length() / n + (my_str.length() % n == 0 ? 0 : 1);
        String[] answer = new String[leng];
        int s = 0, e = n;
        for(int i = 0; i < leng; i++){
            if(e < my_str.length()){
                answer[i] = my_str.substring(s, e);
            } else {
                answer[i] = my_str.substring(s, my_str.length());
            }

            
            s += n;
            e += n;
        }
        return answer;
    }
}