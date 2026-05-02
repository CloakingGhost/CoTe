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
			String[] strArr = br.readLine().split(" ");
			int n = Integer.parseInt(strArr[1]);
			br.close();
			int strLength = strArr[0].length();
			if ((strLength > 0 && strLength < 11) && (n > 0 && n < 6)) {
				for (int i = 0; i < n; i++) {
					wr.write(strArr[0]);
					wr.flush();
				}
				wr.close();
			}
		} catch (NumberFormatException | IOException e) {
			e.printStackTrace();
		}
    }
}