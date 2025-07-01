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