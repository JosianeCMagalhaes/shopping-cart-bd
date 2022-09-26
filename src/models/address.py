async def create_address(address, address_collection):
    address = await address_collection.insert_one(address)
    if address.inserted_id:
            address = await get_address(address_collection, address.inserted_id)
            return address

async def get_address(address_collection, address):
    try:
        data = await address_collection.find_one({address:"_id"})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def find_address(address_collection, cep, address):
    address_collection.find_one({"cep":cep})
    return address

async def del_address(address_collection, _id):
    _id = await address_collection.delete_one({"_id": _id})
    return _id