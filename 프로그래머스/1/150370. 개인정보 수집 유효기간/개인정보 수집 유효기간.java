import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;

public class Solution {
	public int[] solution(String today, String[] terms, String[] privacies) throws ParseException {
		SimpleDateFormat dform = new SimpleDateFormat("yyyy.MM.dd");
		Date nowday = dform.parse(today);
		HashMap<String, Integer> map = new HashMap<>();
		for (int i = 0; i < terms.length; i++) {
			String[] str = terms[i].split(" ");
			map.put(str[0], Integer.parseInt(str[1]));
		}
		ArrayList<Integer> arr = new ArrayList<>();
		for (int i = 0; i < privacies.length; i++) {
			String[] str = privacies[i].split(" ");
			String agreeDay = str[0];
			int month = map.get(str[1]);

			if (nowday.compareTo(calDate(agreeDay, month)) == 1)
				arr.add(i + 1);
		}
		int size = arr.size();
		int[] answer = new int[size];
		for (int i = 0; i < size; i++) {
			answer[i] = arr.get(i);
		}
		return answer;
	}

	private static Date calDate(String agreeDay, int month) throws ParseException {
		SimpleDateFormat dform = new SimpleDateFormat("yyyy.MM.dd");
		Calendar cal = Calendar.getInstance();
		Date dt = dform.parse(agreeDay);
		cal.setTime(dt);
		cal.add(Calendar.MONTH, month);
		cal.add(Calendar.DATE, -1);
		return cal.getTime();
	}
}