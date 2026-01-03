from pydantic import BaseModel
from typing import List, Optional

class Dimensions(BaseModel):
    width: float
    height: float
    depth: float

class Reviews(BaseModel):
    rating: float
    comment: str
    date: str

class Product(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    rating: float
    stock: int
    tags: List[str]
    weight: float

    brand: Optional[str] = None

    dimensions: Dimensions
    reviews: List[Reviews]