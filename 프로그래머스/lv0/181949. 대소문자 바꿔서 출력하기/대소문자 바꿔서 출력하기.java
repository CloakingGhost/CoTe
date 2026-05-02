
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
		try {
			String str = br.readLine();
			br.close();
			int strLength = str.length();
			if (strLength > 0 && strLength < 21) {
				for (char c : str.toCharArray()) {
					if (Character.isLowerCase(c)) {
						c = Character.toUpperCase(c);
					} else {
						c = Character.toLowerCase(c);
					}
					wr.write(c);
				}
			}
			wr.flush();
			wr.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}
}
