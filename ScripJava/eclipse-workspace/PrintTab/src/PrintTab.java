import java.lang.Math.*;
import java.util.Arrays;
import java.util.Scanner;
public class PrintTab {
	
	public static int[] AddElement(int tab[],int x) {
		tab = Arrays.copyOf(tab, tab.length+1);
		tab[tab.length-1]=x;
		return tab;
	}

	public static void main(String[] args) {
		int limiteMax=100;
		int limiteMin =1;
		int range = limiteMax-limiteMin+1;
		
		Scanner sc =new Scanner(System.in);
		int taille = sc.nextInt();
		int tab[]=new int[taille];
		for(int i =0;i<taille;i++ ) {
//			tab=AddElement(tab,(int)(Math.random()*range)+limiteMin);
			tab[i]=(int)(Math.random()*range)+limiteMin;
		}
		String tab2[] = {"salut","bonjour"};
		for(int i =0; i<tab.length; i++)
		{
			System.out.println(tab[i]);
		}
		for(int i =0; i<tab2.length; i++)
		{
			System.out.println(tab2[i]);
		}
	}

}
