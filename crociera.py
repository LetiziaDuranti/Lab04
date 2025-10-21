import csv
from Persona import Persona
from CabinaStandard import CabinaStandard
from CabinaAnimali import CabinaAnimali
from CabinaDeluxe import CabinaDeluxe
from operator import attrgetter
class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome=nome
        self.persone=[]
        self.cabine=[]
    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for riga in reader:
                    if not riga:  # salta le righe vuote
                        continue

                    if riga[0][0]=='C':  # Cabine
                        if len(riga)==4:   # caso cabine standard
                            codice, letti, ponte, prezzo = riga
                            cabina = CabinaStandard(codice, int(letti), int(ponte), float(prezzo))

                        elif riga[4].isdigit():  # caso cabine con animali
                            codice, letti, ponte, prezzo, num_animali = riga
                            cabina = CabinaAnimali(codice, int(letti), int(ponte), float(prezzo), int(num_animali))

                        else:    # caso cabine Deluxe
                            codice, letti, ponte, prezzo, tipo = riga
                            cabina = CabinaDeluxe(codice, int(letti), int(ponte), float(prezzo), tipo)


                        self.cabine.append(cabina)
                    elif riga[0][0]=='P':   # Persone
                        codice, nome, cognome =riga
                        persona=Persona(codice, nome, cognome)
                        self.persone.append(persona)



        except FileNotFoundError:
            raise Exception(f"File {file_path} non trovato.")



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        # cerca la cabina
        cabina = None
        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
                break
        if cabina is None:
            raise Exception(f"Cabina {codice_cabina} non trovata.")

        # verifica disponibilità
        if not cabina.disponibile:
            raise Exception(f"Cabina {codice_cabina} non è disponibile.")

        # cerca il passeggero
        passeggero = None
        for p in self.persone:
            if p.codice == codice_passeggero:
                passeggero = p
                break
        if passeggero is None:
            raise Exception(f"Passeggero {codice_passeggero} non trovato.")

        # verifica che il passeggero non abbia già una cabina
        if passeggero.cabina is not None:
            raise Exception(f"Passeggero {codice_passeggero} ha già una cabina.")

        # assegna la cabina al passeggero e aggiorna la disponibilità
        passeggero.cabina = cabina
        cabina.disponibile = False

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine, key=attrgetter('prezzo_finale'))

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        if not self.persone:
            print("Nessun passeggero registrato.")
            return

        for p in self.persone:
            codice_cabina = p.cabina.codice if p.cabina else "Nessuna"
            print(f"{p.codice} - {p.nome} {p.cognome} | Cabina: {codice_cabina}")

