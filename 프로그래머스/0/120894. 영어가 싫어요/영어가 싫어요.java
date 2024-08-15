class Solution {
    public long solution(String numbers) {
        String[] dic = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] num = {"0", "1", "2", "3", "4", "5", "6", "7" ,"8" ,"9"};
        for(int i = 0; i < dic.length; i++){
            if(numbers.contains(dic[i])){
                numbers = numbers.replaceAll(dic[i], num[i]);
            }
        }
        return Long.parseLong(numbers);
    }
}