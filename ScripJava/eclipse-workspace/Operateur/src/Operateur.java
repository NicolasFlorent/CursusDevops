import java.util.Scanner;


public class Operateur {
	
	
	public static int somme(int a, int b) {
		return a+b;
	}
	
	public static int diff(int a, int b) {
		return a-b;
	}
	
	public static int produit(int a, int b) {
		return a*b;
	}
	
	public static int quotient(int a, int b) {
		return (int)a/b;
	}
	
	public static int reste(int a, int b) {
		return a%b;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		
		System.out.println("La somme est : "+somme(x,y));
		System.out.println("La différence est : "+diff(x,y));
		System.out.println("Le produit est : "+produit(x,y));
		System.out.println("Le quotient est : "+quotient(x,y));
		System.out.println("Le reste de la division euclidienne est : "+reste(x,y));

	}

}
