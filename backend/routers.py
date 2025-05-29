from itertools import product
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()


### Search all items router
@router.get("/products", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    """
    Read all items route
    """
    products = get_products(db)
    return products


### Search item router
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    """
    Read one item route
    """
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
    return db_product


### Add item router
@router.post("/products", response_model=ProductResponse)
def create_a_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Add a new item route
    """
    return create_product(db=db, product=product)


### Delete item router
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_a_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete an item route
    """
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
    return delete_product(product_id=product_id, db=db)


### Update item router
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_a_product(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product does not exist")
    return product_db
