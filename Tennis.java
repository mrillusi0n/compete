import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.util.List;

class Tennis {
	public static void main(String[] args) {
		int[] res = solve(args[0]);
		System.out.printf("%d %d", res[0], res[1]);
		System.out.println();
	}

	static int[] solve(String input) {
		int[] res = new int[2];

		List<Integer> scores = input.replace("L", "0").replace("W", "1")
			.chars()
			.mapToObj(c -> (int) c - '0')
			.collect(Collectors.toList());

		for (int i = 0; i < scores.size(); i++)
			res[i % 2] += scores.get(i);

		return res;
	}
}
