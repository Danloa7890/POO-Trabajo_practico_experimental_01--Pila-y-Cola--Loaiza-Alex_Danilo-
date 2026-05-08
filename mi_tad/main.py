from modelo.pila import Pila
from modelo.cola import Cola

print("=" * 50)
print("   TAD PILA — Comportamiento LIFO")
print("=" * 50)

pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

print(f"Pila inicial:     {pila}")
print(f"Tope (top):       {pila.top()}")
print(f"Extrae (pop):     {pila.pop()}")
print(f"Pila luego pop:   {pila}")
print(f"Tamaño (size):    {pila.size()}")
print(f"¿Vacía?:          {pila.isEmpty()}")

pila2 = Pila()
pila2.push("X")
pila2.push("Y")
pila.pushAll(pila2)
print(f"Luego pushAll:    {pila}")

invertida = pila.reverse()
print(f"Pila invertida:   {invertida}")
print(f"¿Contiene B?:     {pila.contiene('B')}")
print(f"¿Contiene Z?:     {pila.contiene('Z')}")

copia_pila = pila.copiar()
print(f"Copia de pila:    {copia_pila}")
print(f"Pop en copia:     {copia_pila.pop()}")
print(f"Pila original:    {pila}")

print()
print("=" * 50)
print("   TAD COLA — Comportamiento FIFO")
print("=" * 50)

cola = Cola()
cola.push("A")
cola.push("B")
cola.push("C")

print(f"Cola inicial:     {cola}")
print(f"Frente (top):     {cola.top()}")
print(f"Extrae (pop):     {cola.pop()}")
print(f"Cola luego pop:   {cola}")
print(f"Tamaño (size):    {cola.size()}")
print(f"¿Vacía?:          {cola.isEmpty()}")

cola2 = Cola()
cola2.push("X")
cola2.push("Y")
cola.pushAll(cola2)
print(f"Luego pushAll:    {cola}")

invertida_cola = cola.reverse()
print(f"Cola invertida:   {invertida_cola}")
print(f"¿Contiene C?:     {cola.contiene('C')}")
print(f"¿Contiene Z?:     {cola.contiene('Z')}")

copia_cola = cola.copiar()
print(f"Copia de cola:    {copia_cola}")
print(f"Pop en copia:     {copia_cola.pop()}")
print(f"Cola original:    {cola}")