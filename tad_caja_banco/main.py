from modelo.persona import Persona
from caja_banco import CajaBanco
from faker import Faker


def simular_atencion(nombres, titulo_demo, nombre_abandono):
    caja = CajaBanco()

    print("\n" + "=" * 40)
    print(f" {titulo_demo}")
    print("=" * 40)
    print("\nClientes llegando a la fila:\n")

    for nombre in nombres:
        persona = Persona(nombre)
        caja.agregar_persona(persona)
        print(f"  >> Turno #{persona.turno} - {persona.nombre} toma un turno y espera.")

    print("\nUna persona decide retirarse antes de ser atendida:\n")
    resultado = caja.persona_abandona(nombre_abandono)
    print(f"  >> ¿{nombre_abandono} salió de la fila?: {resultado}")
    resultado_inexistente = caja.persona_abandona("Nombre inexistente")
    print(f"  >> ¿Nombre inexistente salió de la fila?: {resultado_inexistente}")

    print("\nCajero listo. Iniciando atención...\n")
    while not caja.esta_vacia():
        persona = caja.atender()
        print(f"  [CAJERO] Turno #{persona.turno} - {persona.nombre} ha sido atendida.")

    print("\nTodos los clientes han sido atendidos.")


def main():
    nombres_manuales = [
        "Pedro Loor",
        "Carmen Intriago",
        "Jorge Menéndez",
        "Valeria Cedeño",
        "Roberto Anchundia",
    ]
    simular_atencion(nombres_manuales, "Banco del Pacífico — Caja #1", "Carmen Intriago")

    fake = Faker("es_ES")
    nombres_automaticos = [fake.name() for _ in range(5)]
    nombre_a_retirar = nombres_automaticos[1]
    simular_atencion(
        nombres_automaticos,
        "Banco del Pacífico — Caja #1 (Utilizando Faker)",
        nombre_a_retirar,
    )

if __name__ == "__main__":
    main()