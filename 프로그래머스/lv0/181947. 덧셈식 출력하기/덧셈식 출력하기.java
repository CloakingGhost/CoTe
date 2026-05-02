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
			String[] nums = br.readLine().split(" ");
			br.close();
			int a = Integer.parseInt(nums[0]);
			int b = Integer.parseInt(nums[1]);
			wr.write(String.format("%d + %d = %d", a, b, a + b));
			wr.flush();
			wr.close();
		} catch (NumberFormatException | IOException e) {
			e.printStackTrace();
		}
    }
}