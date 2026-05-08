class Persona:
    _siguiente_turno = 1

    def __init__(self, nombre):
        self._nombre = nombre
        self._turno = Persona._siguiente_turno
        Persona._siguiente_turno += 1

    @property
    def nombre(self):
        return self._nombre

    @property
    def turno(self):
        return self._turno

    def __str__(self):
        return self._nombre