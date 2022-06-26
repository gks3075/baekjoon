import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int f = b % 10;
		int s = (b / 10) % 10;
		int t = ((b / 10) / 10) % 10;
		System.out.println(a * f);
		System.out.println(a * s);
		System.out.println(a * t);
		System.out.println(a * b);
	}
}