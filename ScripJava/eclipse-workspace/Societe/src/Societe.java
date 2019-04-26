
public class Societe {

	private String nom;
	private String location;
	
	public String getNom() {
		return this.nom;
	}
	
	public String getLocation() {
		return this.location;
	}
	
	public void setNom(String nom) {
		this.nom=nom;
	}
	
	public void setLocation(String location) {
		this.location=location;
	}
	
	public void decrisToi() {
		if(this.nom != "") {
			System.out.println("Nom de ma societe : "+ this.nom);
		}
		if(this.location != "") {
			System.out.println("Localisation : "+this.location);
		}
	}
	
	public Societe(String nom,String location) {
		this.nom=nom;
		this.location=location;
	}
	
	public Societe() {
		this.nom="";
		this.location="";
	}
	
//	public static void main(String[] args) {
//		Societe laSociete;
//		laSociete=new Societe();
//		laSociete.setNom("Google");
//		laSociete.setLocation("Paris");
//		laSociete.decrisToi();
//	}

}
