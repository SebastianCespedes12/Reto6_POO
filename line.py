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
        