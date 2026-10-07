class Prestito:
    def __init__(self, codice, data, id, cognome):
        self.codice = codice
        self.data = data
        self.id = id
        self.cognome = cognome
    def __str__(self):
        return f"{self.codice}, {self.id}, {self.cognome}"