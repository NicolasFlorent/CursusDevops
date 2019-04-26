

public class main {

	public static void main(String[] args) {
		Societe societe1 =new Societe("Google","Paris");
		Employe employe1=new Employe("Google","Toulouse","Marc","PDG",150000);
		Batiment batiment1 = new Batiment("Airbus","Toulouse","56 rue de Tourte, Toulouse","Immeuble");
		
		societe1.decrisToi();
		System.out.println();
		employe1.decrisToi();
		System.out.println();
		batiment1.decrisToi();
	}

}
