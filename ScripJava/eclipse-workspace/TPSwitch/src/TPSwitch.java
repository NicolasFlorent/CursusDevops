import java.util.Scanner;
public class TPSwitch {

	public static void main(String[] args) {
		System.out.println("1. Ouvrir\n2. Quitter\n3. Sauver");
		
		Scanner sc =new Scanner(System.in);
		int choix = sc.nextInt();
		switch(choix) {
		case 1:
			System.out.println("Je n'ai rien à ouvir désolé..");
			break;
		case 2:
			System.out.println("A une prochaine !");
			break;
		case 3:
			System.out.println("Rien à sauver désolé");
			break;
		default:
			System.out.println("Je n'ai pas compris votre choix..");
		}
	}

}
