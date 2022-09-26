from src.models.order import create_order
from src.server.database import connect_db, db, disconnect_db

async def order_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()

    order_collection = db.order_collection

    order = {
            "user": {
                "email": "teste2u@gmail.com",
                "password": "00000045",
                "is_active": True,
                "is_admin": True},
            "paid": True,
            "create": "2016-05-18T16:00:00Z",
            "address": {
                "street" : "Rua Quarenta , Numero 378",
                "cep" : "8465000",
                "district" : "São Paulo",
                "city" : "São Paulo",
                "state" : "São Paulo",
                "is_delivery" : False}
    }

    if option == '1':
        order = await create_order(
            order,
            order_collection
        )
        print("order crated")

    

    await disconnect_db()