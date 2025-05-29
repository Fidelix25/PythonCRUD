from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel


# get all
def get_products(db: Session):
    """
    This function returns all products
    """
    return db.query(ProductModel).all()


# get where id = 1
def get_product(db: Session, product_id: int):
    """
    This function returns one product only
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


# insert into (create)
def create_product(db: Session, product: ProductCreate):
    """
    This function create a new product
    """
    # Transform view to ORM
    db_product = ProductModel(**product.model_dump())
    # Add to table
    db.add(db_product)
    # Table commit
    db.commit()
    # Refresh Database
    db.refresh(db_product)
    # Return the created item
    return db_product


# delete where id = 1
def delete_product(db: Session, product_id: int):
    """
    This function deletes a product
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


# update where id = 1
def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    This function updates product info
    """
    db_product = (
        ProductModel(**product.model_dump())
        .filter(ProductModel.id == product_id)
        .first()
    )

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.supplierEmail is not None:
        db_product.supplierEmail = product.supplierEmail

    db.commit()
    return db_product
