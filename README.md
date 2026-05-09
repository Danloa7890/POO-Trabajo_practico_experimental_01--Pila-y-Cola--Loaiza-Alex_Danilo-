# Trabajo Práctico Experimental 01 — Pila y Cola

## 👤 Información del Equipo

- Carrera: Ingeniería en Software
- Semestre: Cuarto Semestre
- Integrantes:
  - Alex Danilo Loaiza Gomezcuello
  - Michael Alberto Menendez Barzola
  - Marlon Steven Bejarano Muñoz
  - Christian Adolfo Mora Anchundia

## 📖 Estructura del Caso de Estudio

El proyecto se desarrolla siguiendo fases de ingeniería de software:

- Requerimientos: definición de operaciones base y extensiones para estructuras `Pila` y `Cola`, además de una simulación de atención bancaria.
- Análisis: identificación de entidades (`Pila`, `Cola`, `Persona`, `CajaBanco`) y sus interacciones.
- Diseño: modelado UML en PlantUML para ambos subproyectos.
- Desarrollo: implementación en Python con separación por módulos (`modelo`, lógica de dominio y scripts `main.py`).

## 📂 Estructura del Proyecto en el Repositorio

```text
POO-Trabajo_practico_experimental_01--Pila-y-Cola--Loaiza-Alex_Danilo-/
├── mi_tad/
│   ├── main.py
│   ├── modelo/
│   │   ├── pila.py
│   │   └── cola.py
│   └── uml/
│       └── modelado-pila-cola.puml
└── tad_caja_banco/
    ├── main.py
    ├── caja_banco.py
    ├── modelo/
    │   ├── persona.py
    │   └── cola.py
    └── uml/
        └── modelado-caja-banco.puml
```

## Módulos del Proyecto

### 1) `mi_tad` — Implementación de Pila y Cola

Incluye dos estructuras principales:

- `Pila` (comportamiento LIFO)
- `Cola` (comportamiento FIFO)

Funcionalidades implementadas:

- Operaciones base: `push`, `pop`, `top`, `isEmpty`, `size`
- Operaciones adicionales: `pushAll`, `reverse`, `contiene`, `copiar`

### 2) `tad_caja_banco` — Simulación de Atención en Caja

Modela una fila de atención bancaria usando `Cola`, con las clases:

- `Persona`: asigna turno automático correlativo al crear cada instancia.
- `CajaBanco`: agrega personas, atiende en orden FIFO y permite retiro por nombre con `persona_abandona(nombre)`.

## 📦 Dependencias

Este proyecto utiliza la librería **Faker** para generar datos aleatorios en las pruebas. Para instalarla:

```bash
pip install faker
```

Se usó con localización en español (`es_ES`) para generar nombres de clientes de forma automática durante la simulación.
