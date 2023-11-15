import java.util.HashMap;
class Solution {
	public String[] solution(String[] players, String[] callings) {
		HashMap<String, Integer> map = new HashMap<>() {
			{
				for (int i = 0; i < players.length; i++)
					put(players[i], i);
			}
		};
		for (int i = 0; i < callings.length; i++) {
			String name = callings[i];
			int num = map.get(name);
			String temp = players[num];
			players[num] = players[num - 1];
			players[num - 1] = temp;
			map.put(name, map.get(name) - 1);
			map.put(players[num], map.get(players[num]) + 1);

		}
		return players;
	}
}