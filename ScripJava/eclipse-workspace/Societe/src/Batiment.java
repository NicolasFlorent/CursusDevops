
public class Batiment extends Societe{
	
	private String adresse;
	private String type_bat;
	
	public Batiment() {
		super();
		this.adresse="";
		this.type_bat="";
	}
	
	public Batiment(String nom_societe, String location,String adresse, String type) {
		super(nom_societe, location);
		this.adresse=adresse;
		this.type_bat=type;
	}
	
	public void decrisToi() {
		super.decrisToi();
		System.out.println("Adresse de la societe : "+this.adresse);
		System.out.println("Type du batiment : "+this.type_bat);
	}

}
