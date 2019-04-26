package org.eclipse.classes;

import org.eclipse.enumeration.Sport;
import org.eclipse.model.*;

public class Main {

	public static void main(String[] args) {
		Adresse adresse = new Adresse("430 Avenue de Lattre de Tassigny","13009","Marseille");
		Sport monPrefere = Sport.GYM;
		Personne personne = new Personne("Mateus", "Nicolas", 25, adresse, monPrefere);
		System.out.println(personne.toString());
		Biologiste biologiste= new Biologiste("Mateus", "Nicolas", adresse, monPrefere);
		System.out.println(biologiste.toString());
		biologiste.travailler();
		System.out.println(biologiste.toString());
		Biologiste.aimerLaPluie();
		
		
		Biologiste collegue= new Biologiste("Bob", "Thierry", adresse, monPrefere);
		collegue.setCollegueTPBiologiste(biologiste);

		
	}
}
