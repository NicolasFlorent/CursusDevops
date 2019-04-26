
public class Piece {
	
	private int xposition;
	private int yposition;
	private Couleur couleur;
	
	public Piece(int xposition, int yposition, Couleur couleur) {
		this.xposition=xposition;
		this.yposition=yposition;
		this.couleur=couleur;
	}
	
	private int getxposition() {
		return this.xposition;
	}
	
	private int getyposition() {
		return this.yposition;
	}
	
	
	private void setxposition(int xposition) {
		this.xposition=xposition;
	}
	
	private void setyposition(int yposition) {
		this.yposition=yposition;
	}

	
	public void move(int newxposition, int newyposition) {
		this.setxposition(newxposition);
		this.setyposition(newyposition);
	}
	
}
