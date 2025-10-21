from Cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self, codice, posti, ponte, prezzo, stile):
        super().__init__(codice, posti, ponte, prezzo)
        self._stile = stile
# metodi getter e setter
    @property
    def stile(self):
        return self._stile

    @stile.setter
    def stile(self, valore):
        if not valore.strip():
            raise ValueError("Lo stile non può essere vuoto")
        self._stile = valore

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return f"{self._codice}: Animali | {self._letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo}€ - Stile: {self._stile} - {stato}"
    def __repr__(self):
        return f"(codice={self._codice}, letti={self._letti}, ponte={self._ponte}, prezzo={self._prezzo}, stile={self._stile})"
    def calcola_prezzo(self):
        return self._prezzo * 1.20