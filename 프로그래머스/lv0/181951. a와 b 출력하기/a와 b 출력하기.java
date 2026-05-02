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
			String[] strNum = br.readLine().split(" ");
			br.close();
			int num1 = Integer.parseInt(strNum[0]);
			int num2 = Integer.parseInt(strNum[1]);
			if ((num1 >= -100000 && num1 <= 100000) && (num2 >= -100000 && num2 <= 100000)) {
				wr.write("a = " + num1);
				wr.newLine();
				wr.write("b = " + num2);
				wr.flush();
			}
			wr.close();
		} catch (NumberFormatException | IOException e) {
			e.printStackTrace();
		}
    }
}