import java.util.Scanner;
public class InTab {

	public static void main(String[] args) {
		int [] tab = {7,3,4,8,1,9};
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrez une valeur pour savoir si elle est dans le tableau ");
		int a = sc.nextInt();
		boolean test= false;
		for(int i=0;i<tab.length && !test; i++) {
			if (tab[i]==a) {
				System.out.println("La valeur appartient au tableau !");
				test=true;
			}
		}
		if(!test) {
			System.out.println("La valeur n'est pas dans le tableau !");
		}
	}

}
