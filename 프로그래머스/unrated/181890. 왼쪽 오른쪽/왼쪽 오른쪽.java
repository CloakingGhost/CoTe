import java.util.Arrays;
class Solution {
	public String[] solution(String[] str_list) {
		int i = 0;
		for (String str : str_list) {
			if (str.equals("l"))
				return Arrays.copyOf(str_list, i);
			else if (str.equals("r"))
				return Arrays.copyOfRange(str_list, i + 1, str_list.length);
			i++;
		}
		return new String[] {};
	}
}