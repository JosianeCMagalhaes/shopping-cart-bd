async def create_order(order, order_collection):
    try:
        order = await order_collection.insert_one(order)
        if order.inserted_id:
            order = await get_order(order_collection, order.inserted_id)
            return "order crated"

    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order(order_collection, order):
    try:
        data = await order_collection.find_one({order:"_id"})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')


     