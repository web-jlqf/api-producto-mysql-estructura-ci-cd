# services/product_service.py
from models.product_model import (
    insert_product,
    get_all_products,
    delete_product,
    create_table_if_not_exists,
    Product,
)

# Se podría llamar en el arranque
#create_table_if_not_exists()


def add_product(data: dict) -> Product:
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")

    if not name or price is None or stock is None:
        raise ValueError("Faltan campos requeridos: name, price, stock.")

    if price < 0:
        raise ValueError("El precio no puede ser negativo.")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo.")

    return insert_product(name, price, stock)


def list_products() -> list[Product]:
    return get_all_products()


def remove_product(product_id: int) -> None:
    deleted = delete_product(product_id)
    if not deleted:
        raise ValueError("Producto no encontrado.")
