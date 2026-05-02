class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "";
        for(int i = 0; i < db.length; i++){
            String dbId = db[i][0];
            String dbPw = db[i][1];
            if(!id_pw[0].equals(dbId)) {answer = "fail"; continue;}
            if(id_pw[1].equals(dbPw)) return "login";
            else return "wrong pw";
        }
        
        return answer;
    }
}