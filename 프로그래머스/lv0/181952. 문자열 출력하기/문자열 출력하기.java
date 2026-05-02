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

			if (strLength >= 1 && strLength <= 1000000 && !str.contains(" ")) {
				wr.write(str);
				wr.flush();
			}
			wr.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

    }
}