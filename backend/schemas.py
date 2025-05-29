from pydantic import BaseModel, PositiveFloat, EmailStr
from enum import Enum
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    supplierEmail: EmailStr


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    createdAt: datetime

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    supplierEmail: Optional[EmailStr] = None
