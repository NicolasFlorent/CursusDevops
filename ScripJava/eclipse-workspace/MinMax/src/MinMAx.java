import java.lang.Math.*;
import java.util.Scanner;
public class MinMAx {
	
	public static int max(int tab[]) {
		int max=tab[0];
		for(int i =1;i<tab.length;i++) {
			if(tab[i]>max) {
				max=tab[i];
			}
		}
		return max;
	}
	
	public static int min(int tab[]) {
		int min=tab[0];
		for(int i =1;i<tab.length;i++) {
			if(tab[i]<min) {
				min=tab[i];
			}
		}
		return min;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int limiteMax=100;
		int limiteMin= -100;
		int range =limiteMax-limiteMin+1;
		int taille = sc.nextInt();
		int tab[]=new int[taille];
		for(int i =0;i<taille;i++ ) {
			tab[i]=(int)(Math.random()*range)+limiteMin;
			System.out.print(tab[i]+" ");
		}
		System.out.println();
		System.out.println(max(tab));
		System.out.println(min(tab));
		
	}

}
