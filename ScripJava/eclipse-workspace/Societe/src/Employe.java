
public class Employe extends Societe{
	private String statut;
	private String nom_employe;
	private double salaire;
	
	public Employe() {
		super();
		this.statut="";
		this.nom_employe="";
		this.salaire=0;
	}
	
	public Employe(String societe, String location,String nom, String statut, double salaire) {
		super(societe, location);
		this.nom_employe=nom;
		this.statut=statut;
		this.salaire=salaire;
	}
	
	public void decrisToi() {
		System.out.println("Nom de l'employé : "+ this.nom_employe);
		System.out.println("Statut de l'employé : "+ this.statut);
		System.out.println("Salaire de l'employé : "+this.salaire);
		super.decrisToi();
	}
	
}
