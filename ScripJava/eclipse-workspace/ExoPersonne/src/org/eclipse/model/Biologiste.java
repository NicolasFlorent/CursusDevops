package org.eclipse.model;

import org.eclipse.enumeration.Sport;
import org.eclipse.interfaces.Travailleur;

public class Biologiste extends Etudiant implements Travailleur{
	
	protected boolean avoirUneBlouse=false;
	protected Biologiste collegueTPBiologiste;
	
	public Biologiste(String prenom, String nom, Adresse adresse, Sport sport) {
		super(prenom, nom, adresse, sport);
	}

	public void mettreUneBlouse() {
		this.avoirUneBlouse=true;
	}
	
	public static void aimerLaPluie() {
		System.out.println("Nous aimons la pluie");
	}
	
	
	public boolean isAvoirUneBlouse() {
		return avoirUneBlouse;
	}

	public void setAvoirUneBlouse(boolean avoirUneBlouse) {
		this.avoirUneBlouse = avoirUneBlouse;
	}

	public Biologiste getCollegueTPBiologiste() {
		return collegueTPBiologiste;
	}

	public void setCollegueTPBiologiste(Biologiste collegueTPBiologiste) {
		this.collegueTPBiologiste = collegueTPBiologiste;
	}

	@Override
	public void travailler() {		
		this.argent+=2000;
	}

	@Override
	public String toString() {
		return "Biologiste [avoirUneBlouse=" + avoirUneBlouse + ", nom=" + nom + ", prenom=" + prenom + ", age=" + age
				+ ", adresse=" + adresse + ", argent=" + argent + "]";
	}
	
}
