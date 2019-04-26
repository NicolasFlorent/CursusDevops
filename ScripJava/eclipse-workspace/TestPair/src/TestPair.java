import java.util.Scanner;
public class TestPair {

	public static void main(String[] args) {
		System.out.println("Entrez une valeur : ");
		Scanner sc =new Scanner(System.in);
		int a = sc.nextInt();
		if (a%2==0) {
			System.out.println("Le nombre est pair");
		}
		else 
		{
			System.out.println("Le nombre est impair");
		}
		
		
	}

}
