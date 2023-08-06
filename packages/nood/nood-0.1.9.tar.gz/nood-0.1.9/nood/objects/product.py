from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Variant(BaseModel):
    id: Optional[str]
    value: str
    stock: Optional[int]
    atc_url: Optional[str]
    direct_url: Optional[str]

    class Config:
        allow_population_by_field_name = True


class Product(BaseModel):
    site_id: Optional[int]
    url: str
    name: str
    brand: Optional[str]
    price: Optional[float]
    currency: Optional[str]
    sku: Optional[str]
    variants: Optional[List[Variant]] = []
    thumbnail_url: Optional[str]

    class Config:
        allow_population_by_field_name = True
