from itertools import product
from pymongo import MongoClient
async def create_order_items(order_items, order_items_collection):
    try:
        order_items = await order_items_collection.insert_one(order_items)
        if order_items.inserted_id:
            order_items = await get_order_items(order_items_collection, order_items.inserted_id)
            return "order crated"

    except Exception as e:
        print(f'create_order_items.error: {e}')

async def get_order_items(order_items_collection, id_order, product):
    try:
        data = await order_items_collection.find_one({id_order:"_id"})
        if data:
            order_items_collection.insert({product})
            return id_order
    except Exception as e:
        print(f'get_order_items.error: {e}')

