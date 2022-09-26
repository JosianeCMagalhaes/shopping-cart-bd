
async def create_product(product, product_collection):
    try:
        product = await product_collection.insert_one(product)
        if product.inserted_id:
            product = await get_product(product_collection, product.inserted_id)
            return product

    except Exception as e:
        print(f'create_product.error: {e}')

async def get_product(product_collection, product):
    try:
        data = await product_collection.find_one({product:"_id"})
        if data:
            return data
    except Exception as e:
        print(f'get_product.error: {e}')

async def del_product(product_collection, code):
    code = await product_collection.delete_one({"code": code})
    return code