import java.util.Scanner;
public class TestLongueur {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		
		System.out.println("Entrez une chaine de caractère : ");
		String a = sc.nextLine();
		System.out.println("Entrez une chaine de caractère : ");
		String b = sc.nextLine();
		
		System.out.println("La plus grande chaine de caractère est : ");
		if (a.length() > b.length()) {
			System.out.println(a);
		}
		else {
			System.out.println(b);
		}
		
	}

}