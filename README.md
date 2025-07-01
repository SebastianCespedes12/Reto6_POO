# Reto6_POO
## Reto 1
## Pregunta 1.
```python
def operaciones(x:float, y:float, simb:str) -> float:
    try:
        # Validar que los operandos sean números
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Los operandos deben ser números")
        
        # Validar que el símbolo sea válido
        if simb not in ["+", "-", "*", "/"]:
            raise ValueError("Operación no válida. Use: +, -, *, /")
        
        if simb == "+":
            return x + y
        elif simb == "-":
            return x - y
        elif simb == "*":
            return x * y
        elif simb == "/":
            if y == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            return x / y
    finally:
        print("Operación realizada")
```
##Pregunta 2.
```python
def palindromo(palabra: str) -> bool:
    try:
        # Validar que la entrada sea una cadena
        if not isinstance(palabra, str):
            raise TypeError("La entrada debe ser una cadena de texto")
        
        # Validar que la cadena no esté vacía
        if len(palabra) == 0:
            raise ValueError("La cadena no puede estar vacía")
        
        # Convertir a minúsculas y quitar espacios para mejor comparación
        palabra = palabra.lower().replace(" ", "")
        
        longitud = len(palabra)
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - 1 - i]:
                return False
        return True
    finally:
            print("Verificación de palíndromo realizada")
```

##Pregunta 3.
```python
def reconocer_primo(lista: list):
    try:
        # Validar que la entrada sea una lista
        if not isinstance(lista, list):
            raise TypeError("La entrada debe ser una lista")
        
        # Validar que la lista no esté vacía
        if len(lista) == 0:
            raise ValueError("La lista no puede estar vacía")
        
        # Validar que todos los elementos sean enteros
        for elemento in lista:
            if not isinstance(elemento, int):
                raise TypeError(f"Todos los elementos deben ser enteros. Elemento inválido: {elemento}")
        
        lista_primos = []
        for i in lista:
            if i < 2:
                continue
            es_primo = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                lista_primos.append(i)
        return lista_primos
    finally:
        print("Verificación de números primos realizada")
```
##Pregunta 4.
```python
def suma_consecutiva(lista):
    try:
        # Validar que la entrada sea una lista
        if not isinstance(lista, list):
            raise TypeError("La entrada debe ser una lista")
        
        # Validar que la lista tenga al menos 2 elementos
        if len(lista) < 2:
            raise ValueError("La lista debe tener al menos 2 elementos para calcular sumas consecutivas")
        
        # Validar que todos los elementos sean números
        for elemento in lista:
            if not isinstance(elemento, (int, float)):
                raise TypeError(f"Todos los elementos deben ser números. Elemento inválido: {elemento}")
        
        sumas = []
        suma_alta = float('-inf')  # Inicializar con el menor valor posible
        
        for i in range(len(lista) - 1):
            suma = lista[i] + lista[i + 1]
            sumas.append(suma)
            if suma > suma_alta:
                suma_alta = suma
        
        return suma_alta
    finally:
        print("Cálculo de suma consecutiva realizado")
```
##Pregunta 5.
```python
def mismos_caracteres(lista: list):
    try:
        # Validar que la entrada sea una lista
        if not isinstance(lista, list):
            raise TypeError("La entrada debe ser una lista")
        
        # Validar que la lista no esté vacía
        if len(lista) == 0:
            raise ValueError("La lista no puede estar vacía")
        
        # Validar que todos los elementos sean cadenas
        for elemento in lista:
            if not isinstance(elemento, str):
                raise TypeError(f"Todos los elementos deben ser cadenas de texto. Elemento inválido: {elemento}")
            if len(elemento) == 0:
                raise ValueError("Las cadenas no pueden estar vacías")
        
        todas_palabras = {}
        lista_final = []
        for i in lista:
            todas_palabras[f"{i}"] = []
            for j in range(97,123):
                if i.count(chr(j)) > 0:                                
                    todas_palabras[f"{i}"].append(f"{i.count(chr(j))} , {chr(j)}")
        for i in  todas_palabras.items():
            for j in todas_palabras.items():
                if i[0] != j[0] and i[1] == j[1] and i[0] not in lista_final:
                    lista_final.extend([i[0]])
        return lista_final
    finally:
        print("Verificación de palabras con mismos caracteres realizada")
mismos_caracteres([1, "aloh", "adios", "soda", "diosa", "sodai"])
```
## Metodo Point
```python
import math

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        if not isinstance(x, (int, float)):
            raise TypeError(f"La coordenada x debe ser un número, se recibió {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"La coordenada y debe ser un número, se recibió {type(y).__name__}")
        if math.isinf(x):
            raise ValueError("La coordenada x no puede ser infinito")
        if math.isinf(y):
            raise ValueError("La coordenada y no puede ser NaN o infinito")
        
        self.x = float(x)
        self.y = float(y)

    def move(self, new_x: float, new_y: float):
        if not isinstance(new_x, (int, float)):
            raise TypeError(f"La nueva coordenada x debe ser un número, se recibió {type(new_x).__name__}")
        if not isinstance(new_y, (int, float)):
            raise TypeError(f"La nueva coordenada y debe ser un número, se recibió {type(new_y).__name__}")
        if math.isinf(new_x):
            raise ValueError("La nueva coordenada x no puede ser infinito")
        if math.isinf(new_y):
            raise ValueError("La nueva coordenada y no puede ser infinito")
        
        self.x = float(new_x)
        self.y = float(new_y)

    def compute_distance(self, other: "Point") -> float:
        if not isinstance(other, Point):
            raise TypeError(f"El parámetro 'other' debe ser una instancia de Point, se recibió {type(other).__name__}")
        
        distance_squared = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return math.sqrt(distance_squared)
```
## Metodo Line
```python
import math
from Shapes.point import Point

class Line:
    def __init__(self, longitud: float, pendiente: float, punto_inicio: Point, punto_final: Point):
        # Validar tipos de entrada
        if not isinstance(longitud, (int, float)):
            raise TypeError(f"La longitud debe ser un número, se recibió {type(longitud).__name__}")
        if not isinstance(pendiente, (int, float)):
            raise TypeError(f"La pendiente debe ser un número, se recibió {type(pendiente).__name__}")
        if not isinstance(punto_inicio, Point):
            raise TypeError(f"El punto de inicio debe ser una instancia de Point, se recibió {type(punto_inicio).__name__}")
        if not isinstance(punto_final, Point):
            raise TypeError(f"El punto final debe ser una instancia de Point, se recibió {type(punto_final).__name__}")
        
        # Validar que los puntos no sean idénticos
        if punto_inicio.x == punto_final.x and punto_inicio.y == punto_final.y:
            raise ValueError("Los puntos de inicio y final no pueden ser idénticos")
        
        self.longitud = float(longitud)
        self.pendiente = float(pendiente)
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final

    def calcular_longitud(self):
        try:
            distancia = math.sqrt((self.punto_final.x - self.punto_inicio.x) ** 2 + (self.punto_final.y - self.punto_inicio.y) ** 2)
            if math.isinf(distancia):
                raise ValueError("El cálculo de longitud resultó en un valor inválido")
            return distancia
        finally:
            pass
    def calcular_pendiente(self):
        try:
            opuesto = self.punto_final.y - self.punto_inicio.y
            adjacente = self.punto_final.x - self.punto_inicio.x
            
            # Verificar división por cero (línea vertical)
            if adjacente == 0:
                if opuesto > 0:
                    return 90.0  # Línea vertical hacia arriba
                elif opuesto < 0:
                    return 270.0  # Línea vertical hacia abajo
                else:
                    raise ValueError("Los puntos son idénticos, no se puede calcular la pendiente")
            
            angulo = (180 / math.pi) * (math.atan(opuesto / adjacente))
            
            # Verificar que el ángulo sea válido
            if math.isnan(angulo) or math.isinf(angulo):
                raise ValueError("El cálculo de pendiente resultó en un valor inválido")
            
            # Ajustar el ángulo según el cuadrante
            if opuesto > 0 and adjacente > 0:
                return angulo
            if opuesto > 0 and adjacente < 0:
                return 180 - angulo
            if opuesto < 0 and adjacente < 0:
                return 180 + angulo
            if opuesto < 0 and adjacente > 0:
                return 360 - angulo
            
            return angulo
        finally:
            pass
        
```
## Metodo Rectangle
```python
import math
from Shapes.shapes import Shapes
from Shapes.line import Line
from Shapes.point import Point

class Rectangulo(Shapes):
    def __init__(self, vertices, lados, angulos):
        # Validar tipos de entrada
        if not isinstance(vertices, list):
            raise TypeError(f"Los vértices deben ser una lista, se recibió {type(vertices).__name__}")
        if not isinstance(lados, list):
            raise TypeError(f"Los lados deben ser una lista, se recibió {type(lados).__name__}")
        if not isinstance(angulos, list):
            raise TypeError(f"Los ángulos deben ser una lista, se recibió {type(angulos).__name__}")
        
        # Validar que sea un rectángulo (4 vértices, 4 lados, 4 ángulos)
        if len(vertices) != 4:
            raise ValueError(f"Un rectángulo debe tener 4 vértices, se recibieron {len(vertices)}")
        if len(lados) != 4:
            raise ValueError(f"Un rectángulo debe tener 4 lados, se recibieron {len(lados)}")
        if len(angulos) != 4:
            raise ValueError(f"Un rectángulo debe tener 4 ángulos, se recibieron {len(angulos)}")
        
        # Validar que todos los vértices sean instancias de Point
        for vertice in self.vertices:
            if not isinstance(vertice, Point):
                raise TypeError(f"El vértice debe ser una instancia de Point, se recibió {type(vertice).__name__}")
        
        # Validar que todos los lados sean instancias de Line
        for lado in self.lados:
            if not isinstance(lado, Line):
                raise TypeError(f"El lado debe ser una instancia de Line, se recibió {type(lado).__name__}")
        
        # Validar que todos los ángulos sean números válidos
        for angulo in self.angulos:
            if not isinstance(angulo, (int, float)):
                raise TypeError(f"El ángulo debe ser un número, se recibió {type(angulo).__name__}")
            if angulo <= 0 or angulo >= 180:
                raise ValueError(f"El ángulo debe estar entre 0 y 180 grados")
        
        # Validar que los ángulos sumen aproximadamente 360 grados (rectángulo)
        suma_angulos = sum(angulos)
        if abs(suma_angulos - 360) > 1:  # Tolerancia de 1 grado
            raise ValueError(f"La suma de los ángulos de un rectángulo debe ser 360°")
        
        # Validar que tenga 4 ángulos rectos (aproximadamente 90°)
        for angulo in self.angulos:
            if abs(angulo - 90) > 5:  # Tolerancia de 5 grados
                raise ValueError(f"El ángulo {angulo} debe ser aproximadamente 90°°")
        
        super().__init__(vertices, lados, angulos)

    def calcular_area(self):
        try:
            # Validar que tengamos al menos 2 lados para calcular el área
            if len(self.lados) < 2:
                raise ValueError("Se necesitan al menos 2 lados para calcular el área")
            
            base = self.lados[0].calcular_longitud()
            altura = self.lados[1].calcular_longitud()
            
            # Validar que las dimensiones sean positivas
            if base <= 0:
                raise ValueError(f"La base debe ser positiva")
            if altura <= 0:
                raise ValueError(f"La altura debe ser positiva")
            
            # Calcular el área
            area = base * altura
            
            # Validar que el resultado sea válido
            if area <= 0:
                raise ValueError(f"El área calculada debe ser positiva")
            return area
            
        finally:
            pass

```
