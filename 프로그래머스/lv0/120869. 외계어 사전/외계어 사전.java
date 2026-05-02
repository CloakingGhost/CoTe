class Solution {
    public int solution(String[] spell, String[] dic) {
        for(int i = 0; i < dic.length; i++){
            if(dic[i].length() != spell.length) continue;
            for(int j = 0; j < spell.length; j++){
                if(dic[i].contains(spell[j])){
                    dic[i] = dic[i].replaceFirst(spell[j] ,"");
                }
            }
            if(dic[i].isEmpty()){
                return 1; 
            }
        }
        
        return 2;
    }
}