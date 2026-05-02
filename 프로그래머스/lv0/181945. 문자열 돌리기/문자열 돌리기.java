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
			for(int i = 0; i < str.length(); i++) {
				wr.write(str.charAt(i)+"\n");
				wr.flush();
			}
			wr.close();
		} catch (NumberFormatException | IOException e) {
			e.printStackTrace();
		}
    }
}