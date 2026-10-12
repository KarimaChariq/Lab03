from operator import attrgetter
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti={}
        self.prestiti={}
        self.ultimo_id_strumento = 0
        self.ultimo_id_prestito = 0



    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            for riga in f:
                riga = riga.strip()
                if not riga:
                    continue
                campi = riga.split(',')
                if len(campi) == 5:
                    codice = campi[0].strip()
                    tipo = campi[1].strip()
                    marca = campi[2].strip()
                    anno = int(campi[3].strip())
                    valore = float(campi[4].strip())

                    strumento = Strumento(codice, tipo, marca, anno, valore)
                    self.strumenti[codice] = strumento

                    num_id = int(codice[1:])
                    if num_id > self.ultimo_id_strumento:
                        self.ultimo_id_strumento = num_id

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        self.ultimo_id_strumento += 1
        codice = f"S{self.ultimo_id_strumento}"

        strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[codice] = strumento
        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti.values(), key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception(f"Errore: lo strumento con ID {id_strumento} non esiste nel deposito.")

        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception(f"Errore: lo strumento {id_strumento} risulta già in prestito.")

        self.ultimo_id_prestito += 1
        id_prestito = f"P{self.ultimo_id_prestito}"

        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti[id_prestito] = prestito
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception(f"Errore: il codice prestito {id_prestito} non esiste.")
        del self.prestiti[id_prestito]
