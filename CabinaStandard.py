from Cabina import Cabina
class CabinaStandard(Cabina):
    def __init__(self, codice, letti, ponte, prezzo):  # eredita tutto di cabina
        super().__init__(codice, letti, ponte, prezzo)