class Persona:

    def __init__(self, codice, nome, cognome):
        self._codice=codice
        self._nome=nome
        self._cognome=cognome
        self._cabina = None

# metodi getter e setter
    @property
    def codice(self):
        return self._codice  # immutabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valore):
        if not valore.strip():
            raise ValueError("Il nome non può essere vuoto")
        self._nome = valore

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, valore):
        if not valore.strip():
            raise ValueError("Il cognome non può essere vuoto")
        self._cognome = valore

    @property
    def cabina(self):
        return self._cabina

    @cabina.setter
    def cabina(self, valore):
        from Cabina import Cabina
        if valore is not None and not isinstance(valore, Cabina):
            raise ValueError("Deve essere un oggetto Cabina o None")
        self._cabina = valore

    def __str__(self):
        return f"{self._codice}, {self._nome}, {self._cognome}"

    def __repr__(self):
        return f"(codice={self._codice}, nome={self._nome}, cognome={self._cognome})"

    def __eq__(self, other):
        # due passeggeri sono uguali se hanno lo stesso codice
        return self._codice == other._codice

    def __lt__(self, other):
        # ordino alfabeticamente per cognome, poi nome
        if self._cognome == other._cognome:
            return self._nome < other._nome
        return self._cognome < other._cognome