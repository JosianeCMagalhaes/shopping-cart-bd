from src.models.address import(create_address, find_address, del_address)

from src.server.database import connect_db, db, disconnect_db

async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    await connect_db()

    address_collection = db.address_collection

    address = { 
            "street" : "Rua sessenta, Numero 378",
            "cep" : "8465000",
            "district" : "São Paulo",
            "city" : "Salvador",
            "state" : "São Paulo",
            "is_delivery" : False}
           
    
    cep = {"8465000"}

    _id = "6330be7fee0a9c57c4d012ac"


    if option == '1':
        address = await create_address(
            address,
            address_collection
        )
        print(address)

    if option == "2":
        find_address(
            address,
            address_collection,
            cep
        )
        print(address)

    if option == "3":
        address = await del_address(
            address_collection,
            _id
        )
        print("Address Removed")



    await disconnect_db()
