from Cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self, codice, posti, ponte, prezzo, numero_animali):
        super().__init__(codice, posti, ponte, prezzo)
        self._numero_animali = numero_animali
# metodi getter e setter
    @property
    def numero_animali(self):
        return self._numero_animali

    @numero_animali.setter
    def numero_animali(self, valore):
        if valore < 0:
            raise ValueError("Il numero di animali non può essere negativo")
        self._numero_animali = valore

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return f"{self._codice}: Animali | {self._letti} letti - Ponte {self._ponte} - Prezzo {self._prezzo}€ - Max animali: {self._numero_animali} - {stato}"
    def __repr__(self):
        return f"(codice={self._codice}, letti={self._letti}, ponte={self._ponte}, prezzo={self._prezzo}, numero_animali={self._numero_animali})"
    def calcola_prezzo(self):
        return self._prezzo * (1 + 0.10 * self._numero_animali)
