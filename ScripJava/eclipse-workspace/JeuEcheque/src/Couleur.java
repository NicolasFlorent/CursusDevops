
public class Couleur {
	
	public enum Colors{
		Blanc,
		Noir
	}
	Colors couleur;
	
	public Couleur(Colors couleur) {
		this.couleur=couleur;
	}
	
	private Colors getColor() {
		return this.couleur;
	}
	
	private void setColor(Colors couleur) {
		this.couleur=couleur;
	}
}
