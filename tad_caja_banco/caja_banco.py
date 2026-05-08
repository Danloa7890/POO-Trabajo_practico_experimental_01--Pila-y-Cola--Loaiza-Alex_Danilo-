from modelo.cola import Cola

class CajaBanco:

    def __init__(self):
        self._cola = Cola()

    def agregar_persona(self, persona):
        self._cola.push(persona)

    def atender(self):
        return self._cola.pop()

    def persona_abandona(self, nombre):
        cola_aux = Cola()
        eliminado = False

        while not self._cola.isEmpty():
            persona = self._cola.pop()
            if (not eliminado) and persona.nombre == nombre:
                eliminado = True
            else:
                cola_aux.push(persona)

        while not cola_aux.isEmpty():
            self._cola.push(cola_aux.pop())

        return eliminado

    def esta_vacia(self):
        return self._cola.isEmpty()