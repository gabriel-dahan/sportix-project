class Personne:
    def __init__(self, prenom: str, nom: str, age: int, taille: float) -> None:
        if not isinstance(prenom, str):
            raise TypeError("Le prénom doit être une chaîne de caractères")
        self.prenom = prenom

        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une chaîne de caractères")
        self.nom = nom 

        if not isinstance(age, int):
            raise TypeError("L'âge doit être un nombre entier")
        if self.age < 0:
            raise ValueError("L'âge doit être un entier positif")
        self.age = age 

        if not isinstance(taille, float):
            raise TypeError("La taille doit être un réel")
        if self.taille < 0:
            raise ValueError("La taille doit être un réel positif")
        self.taille = taille 

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom} a {self.age} ans et mesure {self.taille} m"

    def conversion(self) -> float: 
        '''
        La fonction permet de convertir la taille en cm en m.
        '''
        return self.taille * 0.01
    
    def __repr__ (self) -> str:
        return f"Personne(prenom: {self.prenom}, nom: {self.nom}, age: {self.age}, taille: {self.taille})"

