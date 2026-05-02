class Solution {
    public String solution(String video_len, //동영상의 길이
                           String pos, //재생위치
                           String op_start, //오프닝 시작 시각
                           String op_end, // 오프닝 종료 시각
                           String[] commands) // 명령어
    {
        int total = timeConverter(video_len);
        int intPos = timeConverter(pos);
        int start = timeConverter(op_start);
        int end = timeConverter(op_end);
        //오프닝 스킵
        
        for(String command : commands) {
            intPos = openingPass(intPos, start, end);
            switch(command){
                case "prev":
                    intPos = prev(intPos);
                    break;
                case "next":
                    intPos = next(intPos, total);                    
                    break;
            }
        }
        intPos = openingPass(intPos, start, end);
        String answer = timeConverter(intPos);
        return answer;
    }
    // 분:초 를
    // 초단위로 바꾼뒤
    //      ":" 으로 split
    //      String[] 생성되면 Integer.parseInt() 실행하여 초에 더함
    //      더한 값은 int total에 저장
    // commands 순회하면서 swtich(){case "prev": break;case "next": break;} 실행
    // 모든 계산이 끝나면
    // pos / 60 => 분 
    // pos % 60 => 초
    // 따라서 "(pos / 60):(pos % 60)" 의 형태로 리턴
    
    private static int prev(int pos){
        //pos < 00:10 이면
        //  pos = "00:00"
        //아니면
        //  pos = pos - 00:10
        if(pos < 10) {
            return 0;
        }
        return pos - 10;
    }
    private static int next(int pos, int video_len){
        //pos < video_len - 00:10 이면
        //  pos = video_len       
        if(pos > video_len - 10){
            return video_len;
        }
        return pos + 10;
    }
    private static int openingPass(int pos, int op_start, int op_end){
        // 가장먼저 실행 되는 함수
        // op_start ≤ pos ≤ op_end 라면
        // pos = op_end

        if(pos >= op_start && pos <= op_end) return op_end;
        return pos;
    }
    private static int timeConverter(String strTime){
        String[] str = strTime.split(":");
        int total = Integer.parseInt(str[0]) * 60 + Integer.parseInt(str[1]);
        
        return total;
    }
    private static String timeConverter(int intTime){
        StringBuilder sb = new StringBuilder();
        int minute = intTime / 60;
        int second = intTime % 60;
        if(minute < 10) sb.append("0");
        sb.append(minute);
        sb.append(":");
        if(second < 10) sb.append("0");
        sb.append(second);
        System.out.println(sb.toString());
        
        return sb.toString();
    }
}
/*
9:17시작
1. 10초 전으로 이동 : "prev"
    현재위치 < 10 처음으로 이동(0분 0초)
2. 10초 후로 이동 : "next"
    남은시간 < 10 마지막으로 이동(video_len)
3. 오프닝 건너뛰기
    op_start ≤ 현재 재생 위치 ≤ op_end
    일 때 끝나는 위치로 이동
    
return "mm:ss"
*/