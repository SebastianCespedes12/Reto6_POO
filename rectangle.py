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
