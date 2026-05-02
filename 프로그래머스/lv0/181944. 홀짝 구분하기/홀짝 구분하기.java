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
			int num = Integer.parseInt(br.readLine());
			br.close();
			wr.write(String.format("%d is %s", num, num % 2 == 0 ? "even" : "odd"));
			wr.flush();
			wr.close();
		} catch (NumberFormatException | IOException e) {
			e.printStackTrace();
		}
    }
}