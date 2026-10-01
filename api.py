from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.inventory import (
    add_product,
    get_product,
    get_all_products,
    update_quantity,
    delete_product
)


app = FastAPI(
    title="Inventory API",
    description="Inventory Management API",
    version="1.0.0"
)


class Product(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int


class QuantityUpdate(BaseModel):
    quantity: int


@app.get("/")
def home():
    return {
        "message": "Inventory API is running"
    }


@app.get("/products")
def get_products():
    return get_all_products()


@app.get("/products/{product_id}")
def get_single_product(product_id: str):
    try:
        product = get_product(product_id)

        return {
            "product_id": product_id,
            **product
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@app.post("/products")
def create_product(product: Product):
    try:
        add_product(
            product.product_id,
            product.name,
            product.price,
            product.quantity
        )

        return {
            "message": "Product added successfully",
            "product_id": product.product_id
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.put("/products/{product_id}")
def update_product_quantity(
    product_id: str,
    data: QuantityUpdate
):
    try:
        update_quantity(
            product_id,
            data.quantity
        )

        return {
            "message": "Quantity updated successfully",
            "product_id": product_id,
            "quantity": data.quantity
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.delete("/products/{product_id}")
def remove_product(product_id: str):
    try:
        delete_product(product_id)

        return {
            "message": "Product deleted successfully",
            "product_id": product_id
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )