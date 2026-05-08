from modelo.persona import Persona
from caja_banco import CajaBanco


def main():
    caja = CajaBanco()

    nombres = [
        "Pedro Loor",
        "Carmen Intriago",
        "Jorge Menéndez",
        "Valeria Cedeño",
        "Roberto Anchundia",
    ]

    print("=" * 40)
    print(" Banco del Pacífico — Caja #1")
    print("=" * 40)

    print("\nClientes llegando a la fila:\n")
    for nombre in nombres:
        persona = Persona(nombre)
        caja.agregar_persona(persona)
        print(f"  >> Turno #{persona.turno} - {persona.nombre} toma un turno y espera.")

    print("\nUna persona decide retirarse antes de ser atendida:\n")
    resultado = caja.persona_abandona("Carmen Intriago")
    print(f"  >> ¿Carmen Intriago salió de la fila?: {resultado}")
    resultado_inexistente = caja.persona_abandona("Nombre inexistente")
    print(f"  >> ¿Nombre inexistente salió de la fila?: {resultado_inexistente}")

    print("\nCajero listo. Iniciando atención...\n")
    while not caja.esta_vacia():
        persona = caja.atender()
        print(f"  [CAJERO] Turno #{persona.turno} - {persona.nombre} ha sido atendida.")

    print("\nTodos los clientes han sido atendidos.")


main()