from Cabina import Cabina
class CabinaStandard(Cabina):
    def __init__(self, codice, posti, ponte, prezzo):  # eredita tutto di cabina
        super().__init__(codice, posti, ponte, prezzo)


