class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        String[] split = s.split("", -1);
        for (String str : split) {
            if (str.isBlank()) {
                sb.append(str);
                count = 0;
            } else {
                if (count % 2 == 0)
                    sb.append(str.toUpperCase());
                else
                    sb.append(str.toLowerCase());
                count++;
            }
        }

        return sb.toString();
    }
}