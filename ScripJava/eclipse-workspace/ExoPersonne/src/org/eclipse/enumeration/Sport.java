package org.eclipse.enumeration;

public enum Sport {
	
	FOOT("FOOT",1),
	RUGBY("RUGBY",2),
	GYM("GYM",3),
	NANTATION("NATATION",4),
	BOXE("BOXE",5),
	COURSE("COURSE",6);
	
	protected final String nom;
	protected final int code;
	
	Sport(String nom, int code){
		this.nom=nom;
		this.code=code;
	}

	public String getNom() {
		return nom;
	}

	public int getCode() {
		return code;
	}
	
	

}
