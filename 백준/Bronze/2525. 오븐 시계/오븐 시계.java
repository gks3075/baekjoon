import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		int t = sc.nextInt();
		int hp = t / 60;
		int mp = t % 60;
		h += hp;
		m += mp;
		if (m > 59) {
			h += 1;
			m -= 60;
		}
		if (h > 23) {
			h -= 24;
		}
		System.out.println(h + " " + m);
	}
}