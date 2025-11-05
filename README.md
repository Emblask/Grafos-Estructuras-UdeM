# Proyecto: Algoritmos de Grafos — Rutas Óptimas y Árbol de Expansión Mínima

## Descripción del proyecto

Este proyecto implementa una clase en Python llamada **GraphMatrix**, que representa un grafo mediante una **matriz de adyacencia**.  
El objetivo es modelar redes de conexión —como carreteras, rutas logísticas o sistemas de distribución— y aplicar sobre ellas algoritmos clásicos de grafos para obtener resultados óptimos.

Las principales funcionalidades incluidas son:

- Construcción de grafos agregando vértices (nodos) y aristas (distancias entre ellos).  
- Visualización de la matriz de adyacencia, mostrando las distancias entre todos los nodos.  
- Cálculo del Árbol de Expansión Mínima (MST) usando el algoritmo de **Prim**, que permite conectar todos los nodos con la menor distancia total posible.  
  - Incluye una representación jerárquica en consola del árbol resultante.  
- Determinación de la ruta más eficiente (TSP) mediante **backtracking**, encontrando el recorrido más corto que visita todos los nodos y regresa al punto de partida.  
- Estimación del costo total del recorrido, considerando el consumo de combustible (diésel) y el rendimiento del vehículo.

---

## Cómo ejecutar el proyecto

### 1. Requisitos
- Python 3.8 o superior instalado.
- No requiere librerías externas (usa solo la biblioteca estándar de Python).

### 2. Ejecución
Guardar el archivo con el código (por ejemplo, **grafo.py**) y ejecútarlo en la terminal con:

```bash
python grafo.py
```

Al ejecutar el script, el programa:
1. Crea un grafo de ejemplo con 5 nodos (A, B, C, D, E).
2. Muestra la matriz de adyacencia.
3. Calcula y muestra el Árbol de Expansión Mínima (MST).
4. Encuentra la ruta más eficiente comenzando desde el nodo "A".

---

## Ejemplo de salida

```
Matriz de adyacencia (km):
   | A | B | C | D | E |
-------------------------
 A | 0 |10 |15 |20 |25 |
 B |10 | 0 |35 |25 |30 |
 C |15 |35 | 0 |30 |20 |
 D |20 |25 |30 | 0 |15 |
 E |25 |30 |20 |15 | 0 |

Aristas seleccionadas:
A — B : 10 km
A — C : 15 km
D — E : 15 km
C — E : 20 km

Distancia total mínima: 60 km
Costo total estimado: 30,000 pesos

Representación del árbol:
A
├── (10 km)
│   └── B
├── (15 km)
│   └── C
│       └── (20 km)
│           └── E
│               └── (15 km)
│                   └── D

Ruta más eficiente: A -> B -> D -> E -> C -> A  
Distancia mínima: 90 km  
Costo total estimado: 45,000 pesos
```

---

## Personalización del grafo

Se puede modificar el bloque final del archivo `.py` para crear nuevos grafos con nodos y distancias deseados.  
Por ejemplo:

```python
grafo = GraphMatrix()
grafo.add_edge("Medellín", "Bogotá", 415)
grafo.add_edge("Medellín", "Cali", 420)
grafo.add_edge("Bogotá", "Barranquilla", 1000)
grafo.add_edge("Cali", "Barranquilla", 1100)
grafo.add_edge("Cali", "Cartagena", 950)

grafo.show_matrix()
grafo.minimum_spanning_tree()
grafo.optimal_route("Medellín")
```

---

## Supuestos asumidos

1. El grafo es no dirigido, es decir, las distancias son simétricas (la distancia A→B es igual a B→A).  
2. No existen aristas con distancia negativa.  
3. Todos los nodos están conectados directa o indirectamente, garantizando que se puede construir un árbol de expansión mínima.  
4. El precio del diésel se asume en 5000 COP por galón, y el rendimiento del vehículo es de 10 km/galón. (ajustable en el __init__)  
5. En la búsqueda de la ruta más eficiente (backtracking), el recorrido inicia y termina en el mismo nodo.  
6. El algoritmo de backtracking tiene complejidad factorial (O(n!)), por lo que se recomienda usarlo con menos de 10 nodos para evitar tiempos de ejecución prolongados.  
7. El usuario puede modificar libremente el grafo y el nodo inicial, adaptando el análisis a diferentes escenarios.


---

## Autor

Proyecto desarrollado por **Miguel Salas** [(github)](github.com/Emblask) como parte del curso de Estructuras de Datos Dinámicas de la UdeM
