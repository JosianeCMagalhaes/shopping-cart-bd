from pydantic import BaseModel
from typing import List

from src.schemas.order import OrderSchema
from src.schemas.product import ProductSchema


class OrderItemSchema(BaseModel):
    order: OrderSchema
    product: List[ProductSchema]
