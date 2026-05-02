
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {

	public static void main(String[] args) {
		BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));

		try {
			wr.write("!@#$%^&*(\\'\"<>?:;");
			wr.flush();
			wr.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
