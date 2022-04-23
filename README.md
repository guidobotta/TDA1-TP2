# TP2 Algonautas

https://docs.google.com/document/d/1L5YFJh4rSsyc56rMmYdFXI9yif9FxhQu5n4bznjL_x0/edit#

# Uso

```sh
python3 parte2.py <ruta_archivo.txt>
```

# Casos de Prueba

Se realizaron distintos casos de prueba. Para cada caso se incluyen los resultados esperados. Los nodos del ciclo puede que se impriman en otro orden al esperado. En caso de existir múltiples ciclos, uno de ellos debe coincidir con la salida.

**catedra**

Nodos del ciclo: [E, D, A] 

Costo: -1

**completo_con_ciclo_negativo_1**

Nodos del ciclo: [B, C, D]

Costo: -3

**completo_con_ciclo_negativo_2**

Nodos del ciclo: [B, C, D] 

Costo: -3

Nodos del ciclo: [A, B, C, D] 

Costo: -4

**completo_sin_ciclo_negativo_1**

Sin ciclo

**completo_sin_ciclo_negativo_2**

Sin ciclo

**con_bucle_negativo1**

Nodos del ciclo: [A]

Costo: -1

**con_bucle_negativo2**

Nodos del ciclo: [C]

Costo: -1

**con_bucle_positivo1**

Sin ciclo

**con_bucle_positivo2**

Sin ciclo

**con_ciclo_negativo1**

Nodos del ciclo: [A, B, C, D] 

Costo: -4

**con_ciclo_negativo2**

Nodos del ciclo: [C, D] 

Costo: -2

**con_ciclo_negativo3**

Nodos del ciclo: [C, D, F, G] 

Costo: -2

**con_ciclo_negativo4**

Nodos del ciclo: [F, D, B, E] 

Costo: -3

**gran_ciclo_negativo**

Nodos del ciclo: [D, E, A, B, C] 

Costo: -1

**sin_ciclos_negativos**

Nada

**sin_ciclos_negativos2**

Nada

**sin_ciclos_negativos3**

Nada

**multiples_ciclos_negativos**

Nodos del ciclo 1: [C, D]

Costo: -2

Nodos del ciclo 2: [E, F]

Costo: -1

**isla_negativa**

Nada
