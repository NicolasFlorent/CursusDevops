
public class Case {
	private int xposition;
	private int yposition;
	private String statut;
	private Couleur couleur;
	
	public Case(int xposition, int yposition, String statut,Couleur couleur) {
		this.xposition=xposition;
		this.yposition=yposition;
		this.statut=statut;
		this.couleur=couleur;
	}
	
	private int getxposition() {
		return this.xposition;
	}
	
	private int getyposition() {
		return this.yposition;
	}
	private String getStatut() {
		return this.statut;
	}
	
	private void setxposition(int xposition) {
		this.xposition=xposition;
	}
	
	private void setyposition(int yposition) {
		this.yposition=yposition;
	}
	private void setStatut(String statut) {
		this.statut=statut;
	}
	
	
	
	
}
