import java.util.Scanner;
public class SumWhile {

	public static void main(String[] args) {
		int askNum=0;
		int sum=0;
		Scanner sc =new Scanner(System.in);
		while(askNum!=-1) {
			askNum=sc.nextInt();
			sum += askNum;
		}
		System.out.println("La somme des nombres précédents est "+sum);
	}

}
