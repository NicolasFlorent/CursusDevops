package org.eclipse.model;

import org.eclipse.enumeration.Sport;
import org.eclipse.interfaces.Travailleur;

public class Etudiant extends Personne{
	public Etudiant(String prenom, String nom, Adresse adresse, Sport sport) {
		super(prenom, nom, 20,adresse, sport);
		// TODO Auto-generated constructor stub
	}

	public void afficherDetails(){
		System.out.println(nom + " " + prenom);
	}
	
}
