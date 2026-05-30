from dataclasses import dataclass

@dataclass
class Product:
    title : str
    price : float
    discription : str
    image: str
    category : str
