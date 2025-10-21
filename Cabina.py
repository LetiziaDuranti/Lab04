class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self._codice=codice
        self._letti=letti
        self._ponte=ponte
        self._prezzo=prezzo
        self._disponibile = True # tutte le cabine partono libere

# metodi getter e setter
    @property
    def codice(self):
        return self._codice  # immutabile

    @property
    def letti(self):
        return self._letti

    @property
    def ponte(self):
        return self._ponte

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, valore):
        if valore < 0:
            raise ValueError("Il prezzo non può essere negativo")
        self._prezzo = valore

    @property
    def disponibile(self):
        return self._disponibile

    @disponibile.setter
    def disponibile(self, valore):
        if not isinstance(valore, bool):
            raise ValueError("Disponibile deve essere True o False")
        self._disponibile = valore

    @property
    def prezzo_finale(self):
        return self.calcola_prezzo()

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return f"{self._codice}: Standard | {self._letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo}€ - {stato}  "

    def __repr__(self):
        return f"(codice={self._codice}, letti={self._letti}, ponte={self._ponte}, prezzo={self._prezzo})"

    def calcola_prezzo(self):
        # Restituisce il prezzo della cabina base
        return self._prezzo

    def __eq__(self, other):
        # due cabine sono uguali se hanno lo stesso codice
        return self._codice == other._codice

    def __lt__(self, other):
        # prima confronto per prezzo crescente
        if self.calcola_prezzo() == other.calcola_prezzo():
            # in caso di parità, ordino per codice
            return self._codice < other._codice
        return self.calcola_prezzo() < other.calcola_prezzo()