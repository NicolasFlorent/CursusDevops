import java.util.Scanner;

public class TestNegatif {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		if((a<0 && b<0) || (a>0 && b>0)){
			System.out.println("Le produit est positif");
		}
		else if ((a<0 && b>0) || (a>0 && b<0)) {
			System.out.println("Le produit est negatif");
		}
		else {
			System.out.println("Le produit est nul");
		}
	}

}
