# routers/product_router.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.product_service import add_product, list_products, remove_product

router = APIRouter(prefix="/products", tags=["products"])

# Schema de entrada/salida
class ProductIn(BaseModel):
    name: str
    price: float
    stock: int


class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    stock: int


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductIn):
    try:
        new_product = add_product(product.dict())
        return ProductOut(
            id=new_product.id,
            name=new_product.name,
            price=new_product.price,
            stock=new_product.stock,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[ProductOut])
def get_products():
    products = list_products()
    return [
        ProductOut(
            id=p.id,
            name=p.name,
            price=p.price,
            stock=p.stock,
        )
        for p in products
    ]


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    try:
        remove_product(product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
