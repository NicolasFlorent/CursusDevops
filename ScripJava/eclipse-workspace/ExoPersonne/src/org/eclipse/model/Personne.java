package org.eclipse.model;

import org.eclipse.enumeration.Sport;

public class Personne{
	protected String nom;
	protected String prenom;
	protected int age;
	protected Adresse adresse;
	protected int argent =1000;
	protected Sport sport;

	public Personne(String prenom, String nom, int age, Adresse adresse, Sport sport) {
		this.prenom = prenom;
		this.nom = nom;
		this.age = age;
		this.adresse=adresse;
		this.sport=sport;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		if (age >= 0)
			this.age = age;
		else 
			this.age = 0;
	}
	
	public Adresse getAdresse() {
		return adresse;
	}

	public void setAdresse(Adresse adresse) {
		this.adresse = adresse;
	}

	public String toString() {
		return prenom+" "+nom+", "+age+"ans, habite a l'adresse "+adresse;
	}
}
